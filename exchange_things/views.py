from django.contrib.auth.admin import UserAdmin
from django.db.utils import OperationalError
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .forms import RegisterUserForm,AdForm
from .models import Ad,Category


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    next_page = '/'


class RegisterUser(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        username = form.save()
        login(self.request, username)
        return super().form_valid(form)


def profile(request):
    return render(request, 'accounts/profile.html')


def custom_404_view(request, *args, **kwargs):
    return TemplateResponse(request, '404.html', status=404)


def index(request):
    try:
        ad_db = Ad.objects.all()
        # for card in ad_db:
        #     print(f'{card.id}: {card.title}')

        context = {'ad_db': ad_db}
        return render(request, 'index.html', context=context)
    except Ad.DoesNotExist:
        return TemplateResponse(request, '404.html')
    except OperationalError:
        return TemplateResponse(request, '404.html')


def ad(request):
    outperform = AdForm()
    # try:
    categories = Category.objects.all()
    context = {'categories': categories}
    # success_url = '/'
    if request.method == "POST":
        outperform = AdForm(request.POST)
        if outperform.is_valid():
            pass
    return render(request, "ad/ad.html", {"form": outperform})
    # return TemplateResponse(request, "ad/ad.html")

    # except Category.DoesNotExist:


def account(request):
    return TemplateResponse(request, "accounts/profile.html")


def exchange(request):
    return TemplateResponse(request, "ad/exchange.html")
