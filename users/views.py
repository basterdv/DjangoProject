import requests
from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from users.forms import RegisterUserForm, ProfileForm, LoginUserForm


class Login(LoginView):
    template_name = 'users/login.html'
    # form_class = AuthenticationForm
    form_class = LoginUserForm

    # redirect_authenticated_user = True
    # success_url = reverse_lazy('home')
    # success_url = '/'

    # def get(self,request, *args, **kwargs):
    #     code = request.GET.get('code')
    #     expires_in = request.GET.get('expires_in')
    #     device_id = request.GET.get('device_id')
    #     state = request.GET.get('state')
    #     ext_id = request.GET.get('ext_id')
    #     type =  request.GET.get('type')
    #
    #     print(f'code - {code}')
    #     print(f'expires_in - {expires_in}')
    #     print(f'device_id - {device_id}')
    #     print(f'state - {state}')
    #     print(f'ext_id - {ext_id}')
    #     print(f'type - {type}')

    # return super(Login, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация | Обменник'
        return context

    def get_success_url(self):
        return reverse_lazy('main:index')

    def form_invalid(self, form):
        messages.error(self.request, "Неверный логин или пароль")  # Добавляем сообщение об ошибке
        return self.render_to_response(self.get_context_data(context={'form': form}))

    def form_valid(self, form):
        # Perform custom actions here before calling super().form_valid()

        login(self.request, form.get_user())  # Log the user in
        return super().form_valid(form)


# class Logout(LogoutView):
#     next_page = '/'

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

    # user = CustomUser.objects.get(pk=request.user.pk)
    # user = CustomUser.objects.filter(username=request.user.username).first()
    user_id = request.user
    # user = CustomUser.objects.filter(user_id=request.user)
    # print(user_id)

    context = {
        # 'user': user,
        'form': form,
        'title': 'Ghjabkm'
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

@csrf_exempt
def vk_auth_callback(request):
    code = request.GET.get('code')
    device_id = request.GET.get('device_id')
    _type = request.GET.get('type')
    expires_in =request.GET.get('expires_in')
    # print(code)
    # print(device_id)
    # print(_type)
    # print(expires_in)

    TOKEN_EXCHANGE_URL = 'https://id.vk.com/oauth2/auth'
    payload = {
        # 'client_id': client_id,
        # 'client_secret': client_secret,
        # 'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'client_id': 54015625,
        'device_id': device_id,
        'code': code,
        'redirect_uri': 'http://localhost/users/vk_auth_callback',
        'verifier': 'code_verifier',
        # 'grant_type': 'authorization_code'
    }

    # Отправляем POST-запрос к VK API
    # print(payload)
    response = requests.post(TOKEN_EXCHANGE_URL, data=payload)
    print(response.json())

    template_name = 'users/vk_auth_callback.html'

    # if not code:
    #     print("Ошибка авторизации: отсутствует код")
    # return HttpResponse("Ошибка авторизации: отсутствует код")
    # return redirect(request, 'users/profile.html')
    return render(request, template_name)
    # return redirect(request, 'users/vk_auth_callback.html')

#     # vk_session = VkApi(app_id=settings.VK_APP_ID, app_secret=settings.VK_APP_SECRET,
#     #                    redirect_uri=settings.VK_REDIRECT_URI)
#     # try:
#     #     vk_session.auth(code=code)
#     # except Exception as e:
#     #     # return HttpResponse(f"Ошибка авторизации: {e}")
#     #     print('fault')
#
#     # vk = vk_session.get_api()
#     # try:
#         user_info = vk.users.get(fields='first_name,last_name,photo_max_orig')  # Получение данных пользователя
#         # Обработка данных пользователя
#         # Создание или вход пользователя в Django
#         # Например:
#         # user, created = User.objects.get_or_create(username=user_info[0]['id'])
#         # user.first_name = user_info[0]['first_name']
#         # user.last_name = user_info[0]['last_name']
#         # user.save()
#         # login(request, user)
#
#     # except Exception as e:
#     #     print('fault')
#         # return HttpResponse(f"Ошибка получения данных пользователя: {e}")
#
#     # return HttpResponse("Авторизация успешна! Данные пользователя: {}".format(user_info))
#
#
# # def vk_auth_start(request):
# #     vk_session = VkApi(app_id=settings.VK_APP_ID, scope='email')
# #     auth_url = vk_session.get_auth_url(settings.VK_REDIRECT_URI, get_random_id())
# #     return redirect(auth_url)
