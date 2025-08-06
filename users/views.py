from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from users.forms import RegisterUserForm, ProfileForm, LoginUserForm


class Login(LoginView):
    template_name = 'users/login.html'
    # form_class = AuthenticationForm
    form_class = LoginUserForm

    # redirect_authenticated_user = True
    # success_url = reverse_lazy('home')
    # success_url = '/'

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

#
#
