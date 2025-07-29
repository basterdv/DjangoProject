from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from main.forms import RegisterUserForm


class Login(LoginView):
    template_name = 'users/login.html'

    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

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

class RegisterUser(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        username = form.save()
        login(self.request, username)
        return super().form_valid(form)

def profile(request):
    return render(request, 'users/profile.html')