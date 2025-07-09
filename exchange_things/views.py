from urllib.parse import uses_query

from django.contrib.auth.admin import UserAdmin
from django.db.utils import OperationalError
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .forms import RegisterUserForm,AdForm
from .models import Advert,Category,CustomUser


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
        ad_db = Advert.objects.all()
        # for card in ad_db:
        #     print(f'{card.id}: {card.title}')

        context = {'ad_db': ad_db}
        return render(request, 'index.html', context=context)
    except Advert.DoesNotExist:
        return TemplateResponse(request, '404.html')
    except OperationalError:
        return TemplateResponse(request, '404.html')


def ad(request):

    if request.method == 'POST' and 'submit_ad_form' in request.POST:
        ad_form = AdForm(request.POST, request.FILES)
        if ad_form.is_valid():

            if request.user.is_authenticated:
                us_id = CustomUser.objects.get(id=request.user.id)
                # user_id = request.user.id
                my_instance = ad_form.save(commit=False)
                parent_instance = CustomUser.objects.get(id=request.user.id)
                my_instance.user_id = parent_instance
                my_instance.save()  # Saves the data to the database
                return redirect('/')
    else:
        ad_form = AdForm()

    return render(request, "ad/ad.html", {'ad_form': ad_form})
    # ad_form = AdForm()
    #
    # categories = Category.objects.all()
    #
    # # context = {'categories': categories}
    # # success_url = '/'
    # if request.method == "POST":
    #     print('post')
    #     if 'submit_ad_form' in request.POST:
    #         outperform = AdForm(request.POST)
    #         if outperform.is_valid():
    #             return redirect('/')
    # context = {'ad_form':ad_form}
    # return render(request, "ad/ad.html", context=context)
    # # return TemplateResponse(request, "ad/ad.html")
    #
    # # except Category.DoesNotExist:


def account(request):
    return TemplateResponse(request, "accounts/profile.html")


def exchange(request):
    return TemplateResponse(request, "ad/exchange.html")
