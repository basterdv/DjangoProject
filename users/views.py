import logging
from datetime import datetime

import requests
from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.generic import FormView
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


class PasswordReset(FormView):
    template_name = 'users/password-reset.html'
    form_class = PasswordResetForm

    def get_context_data(self, **kwargs):
        context = super(PasswordReset, self).get_context_data(**kwargs)
        context['title'] = 'Восстановление пароля | Обменник'
        return context


def google_auth_callback(request):
    email = 'baster12@list.ru'
    user = CustomUser.objects.get(email=email)

    login(request, user)
    return render(request, 'users/login.html')
    # return redirect(request, 'users/login.html')


@method_decorator(csrf_exempt, name='dispatch')
class VKAuthView(LoginView):
    template_name = 'users/login.html'

    def post(self, request, *args, **kwargs):
        access_token = request.POST.get('access_token')
        id_token = request.POST.get('id_token')

        if not access_token or not id_token:
            logger.error('Access token or ID token missing')
            return JsonResponse({'status': 'error', 'message': 'Access token or ID token missing'}, status=400)

        # URL для обмена публичными данными пользователя
        USER_PUBLIC_DATA_EXCHANGE_URL = 'https://api.vk.com/method/users.get'

        # Параметры запроса для получения публичных данных пользователя
        payload_public = {
            'access_token': access_token,
            'fields': 'first_name,last_name',
            'v': '5.131',  # Укажите версию API ВКонтакте
        }

        # Отправляем GET-запрос для получения публичных данных пользователя
        response_public = requests.get(USER_PUBLIC_DATA_EXCHANGE_URL, params=payload_public)

        if response_public.status_code != 200:
            logger.error('Error for public data request: %s', response_public.json())
            return JsonResponse(
                {'status': 'error', 'message': 'Error in public data request', 'details': response_public.json()},
                status=response_public.status_code)

        data_user_public_info = response_public.json()
        # print(data_user_public_info)

        if 'error' in data_user_public_info:
            return JsonResponse({'status': 'error', 'message': 'Error in public data request',
                                 'details': data_user_public_info['error']}, status=400)

        # URL для обмена личными данными пользователя
        USER_PRIVATE_DATA_EXCHANGE_URL = 'https://api.vk.com/method/users.get'

        # Параметры запроса для получения личных данных пользователя
        payload_private = {
            'access_token': access_token,
            'fields': 'email,bdate',
            'v': '5.131',  # Укажите версию API ВКонтакте
        }

        # Отправляем GET-запрос для получения личных данных пользователя
        response_private = requests.get(USER_PRIVATE_DATA_EXCHANGE_URL, params=payload_private)

        if response_private.status_code != 200:
            logger.error('Error for private data request: %s', response_private.json())
            return JsonResponse(
                {'status': 'error', 'message': 'Error in private data request', 'details': response_private.json()},
                status=response_private.status_code)

        data_user_private_info = response_private.json()
        # print(data_user_private_info)

        if 'error' in data_user_private_info:
            return JsonResponse({'status': 'error', 'message': 'Error in private data request',
                                 'details': data_user_private_info['error']}, status=400)

        # Дополнительная логика для обработки данных
        # ...

        # Предполагается, что у вас есть пользовательская логика для создания или аутентификации пользователя
        # Например, вы можете создать пользователя или аутентифицировать существующего пользователя
        user = self.authenticate_via_vk(access_token, id_token)

        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'url': reverse_lazy('main:index').url})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to authenticate via VK'}, status=401)

    def authenticate_via_vk(self, access_token, id_token):
        # Ваша логика для аутентификации через VK
        # Например, вы можете использовать данные из response_public и response_private
        # для создания или поиска пользователя в базе данных
        # Замените это на вашу реализацию
        return None  # Возвращаем None, если аутентификация не удалась


@csrf_exempt
@requires_csrf_token
def vk_auth_callback(request):
    try:
        code = request.GET.get('code')
        device_id = request.GET.get('device_id')
        _type = request.GET.get('type')
        expires_in = request.GET.get('expires_in')
        # code_verifier = request.GET.get('code_verifier')
        state = request.GET.get('state')

        code_verifier = 'b5i9j_JQn3YeOlghVuS4WgdKcjoMIpJ7jFiOBO7QKSAxXa42HKu90hpMWQTL6F1KyoRrCD7Uw2H2u6mCQTJm-FMHro-NOYyhaPTsZqdkyFAvM85WGu0wa4g47SNOdyXW'

        TOKEN_EXCHANGE_URL = 'https://id.vk.com/oauth2/auth'
        USER_PUBLIC_DATA_EXCHANGE_URL = 'https://id.vk.com/oauth2/public_info'
        USER_INFO_DATA_EXCHANGE_URL = 'https://id.vk.com/oauth2/user_info'

        payload = {
            'grant_type': 'authorization_code',
            'client_id': 54015625,
            'device_id': device_id,
            'code': code,
            'redirect_uri': 'http://localhost/users/vk_auth_callback',
            'code_verifier': code_verifier,
            # 'state': state,

        }

        # Отправляем POST-запрос к VK API
        # print(payload)
        response = requests.post(TOKEN_EXCHANGE_URL, data=payload,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        data = response.json()

        print(data)
        if 'access_token' in data:
            # print(response.json())
            access_token = data['access_token']
            id_token = data['id_token']
            expires_in = data['expires_in']
            # print(access_token)
            # print(id_token)
            # print(expires_in)

            # Отправляем POST-запрос для получения публичных данных пользователя
            payload = {
                'client_id': 54015625,
                'id_token': id_token,
            }

            response = requests.post(USER_PUBLIC_DATA_EXCHANGE_URL, data=payload,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
            data_user_public_info = response.json()
            # print(data_user_public_info)

            # Отправляем POST-запрос для получения личных данных пользователя
            payload = {
                'client_id': 54015625,
                'access_token': access_token,
            }

            response = requests.post(
                USER_INFO_DATA_EXCHANGE_URL,
                data=payload,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            data_user_info = response.json()
            # print(data_user_info)
            user_id = data_user_info['user']['user_id']
            email = data_user_info['user']['email']
            first_name = data_user_info['user']['first_name']
            last_name = data_user_info['user']['last_name']
            avatar = data_user_info['user']['avatar']
            birthday = data_user_info['user']['birthday']

            username = email
            # Поиск или создание пользователя в базе данных
            try:
                user = CustomUser.objects.get(email=email)
                logger.info(f'Пользователь с почтой {email} найден')
                # login(request, username) # Логинимся
            except:
                logger.error(f'Пользователь с потной {email} не найден')
                user = CustomUser.objects.create_user(
                    username=first_name,
                    email=email
                )
            # Логинимся
            user.first_name = first_name
            user.last_name = last_name
            user.avatar = avatar
            user.birthday = datetime.strptime(birthday, '%d.%m.%Y').date().strftime('%Y-%m-%d')

            user.username = first_name
            user.set_password(user_id)
            user.save()

            login(request, user)

        else:
            logger.error(f'error')

        template_name = 'users/vk_auth_callback.html'

        return render(request, template_name)
    except:
        template_name = 'users/login.html'
        logger.error(f'error')
        return render(request, template_name)


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


class OAuthCallbackView(BaseFormView):
    def get(self, request):
        code = self.request.GET.get('code')
        cid = request.GET.get('cid')
        provider = request.GET.get('provider', 'google')

        if provider == 'yandex':
            user_data = YandexProvider().get_user_info(code)
        elif provider == 'vk':
            user_data = VkProvider().get_user_info(code)
        else:
            logger.error(f'error:Invalid provider')
            return redirect('/users/login')

        if user_data is not None:
            user_id = int(user_data['id'])
            email = user_data['email']
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            avatar = user_data['default_avatar_id']
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
                # user.birthday = datetime.strptime(birthday, '%d.%m.%Y').date().strftime('%Y-%m-%d')

                user.username = username
                user.set_password(str(user_id))
                user.save()
                login(request, user)
            except:
                logger.error(f'Ошибка авторизации')

        return redirect('/users/login')
