import logging
from datetime import datetime

import requests
from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.generic import FormView, TemplateView
from django.views.generic.edit import BaseFormView
from requests import Response

from users.auth.providers.yandex import YandexProvider
from users.auth.providers.vk import VkProvider
from users.forms import RegisterUserForm, ProfileForm, LoginUserForm
from users.models import CustomUser

logger = logging.getLogger(__name__)


# @method_decorator(csrf_exempt, name='dispatch')
class Login(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('main:index'))  # Перенаправлять на главную страницу
        return super(Login, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация | Обменник'
        return context

    def get_success_url(self):
        return reverse_lazy('main:index')

    def form_invalid(self, form):
        print('invalid')
        logout(self.request)
        self.request.session.flush()
        messages.error(self.request, "Неверный логин или пароль")  # Добавляем сообщение об ошибке
        return super().form_invalid(form)

    def form_valid(self, form):
        # Perform custom actions here before calling super().form_valid()

        login(self.request, form.get_user())  # Log the user in
        return super().form_valid(form)


@login_required
def logout(request):
    # messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))


class RegisterUserView(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterUserForm
    # success_url = reverse_lazy('home')
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(RegisterUserView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация | Обменник'
        return context

    def form_valid(self, form):
        username = form.save()
        login(self.request, username)
        return super().form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect(request, 'users/profile.html')
    else:
        form = ProfileForm(instance=request.user)

    # user = get_object_or_404(CustomUser, pk=user_id)

    user = CustomUser.objects.get(pk=request.user.pk)

    context = {
        # 'user': user,
        'form': form,
        'title': 'Профиль пользователя'
    }
    return render(request, 'users/profile.html', context)
    # return render(request, 'users/profile.html', context)


class UserProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'users/profile.html'
    # login_url = 'users/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:

            try:
                profile = CustomUser.objects.get(pk=user.pk)
                context = {
                    # 'user': user,
                    'form': profile,
                    'title': 'Профиль пользователя'
                }
            except CustomUser.DoesNotExist:
                # Обработка случая, когда профиль пользователя не существует
                logger.warning(f'Profile does not exist for user {user.username}')
                context['profile'] = None

            return context
        else:
            # Обработка случая, когда пользователь не авторизован
            logger.warning('Accessing user profile without authentication')
            context['profile'] = None
            return redirect(reverse('main:index'))

    # def get_object(self):
    #     return CustomUser.objects.get(pk=self.request.user.pk)


class PasswordReset(FormView):
    template_name = 'users/password-reset.html'
    form_class = PasswordResetForm

    def get_context_data(self, **kwargs):
        context = super(PasswordReset, self).get_context_data(**kwargs)
        context['title'] = 'Восстановление пароля | Обменник'
        return context


class OAuthBaseView(BaseFormView):
    provider_class = None

    def get(self, request):
        provider = self.provider_class()
        auth_url = provider.get_auth_url()
        return redirect(auth_url)


class YandexOAuthView(OAuthBaseView):
    provider_class = YandexProvider


class VKOAuthView(OAuthBaseView):
    provider_class = VkProvider


class OAuthCallbackView(View):
    def get(self, request, provider):
        code = self.request.GET.get('code')
        device_id = request.GET.get('device_id')

        if provider == 'yandex':
            user_data = YandexProvider().get_user_info(code)
        elif provider == 'vk':
            user_data = VkProvider().get_user_info(code, device_id)
        else:
            logger.error(f'error:Invalid provider')
            return redirect('/users/login')

        if user_data is not None:
            user_id = int(user_data['id'])
            email = user_data['email']
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            avatar = user_data['avatar_id']
            birthday = user_data['birthday']
            username = user_data['login']

            # Поиск или создание пользователя в базе данных
            try:
                user = CustomUser.objects.get(email=email)
                logger.info(f'Пользователь с почтой {email} найден')
            except:
                logger.error(f'Пользователь с почтой {email} не найден')
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email
                )

            # Логинимся
            try:
                user.first_name = first_name
                user.last_name = last_name
                user.avatar = avatar
                user.birthday = birthday

                user.username = username
                user.set_password(str(user_id))
                user.save()
                login(request, user)
            except:
                logger.error(f'Ошибка авторизации')

        return redirect('/users/login')
