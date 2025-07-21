from urllib.parse import uses_query

from django.contrib import auth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .forms import RegisterUserForm, AdvertForm
from .models import Advert, Category, CustomUser


class Login(LoginView):
    template_name = 'accounts/login.html'


# class Logout(LogoutView):
#     next_page = '/'

@login_required
def logout(request):
    # messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('index'))

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

@login_required # Будет выполнятся только для зарег пользов
def advert(request):
    if request.method == 'POST':
        advert_form = AdvertForm(data=request.POST, files=request.FILES, )
        #                          instance=CustomUser.objects.get(id=request.user.id))

        if advert_form.is_valid():

            # if request.user.is_authenticated:
                # us_id = CustomUser.objects.get(id=request.user.id)
                # user_id = request.user.id

            my_instance = advert_form.save(commit=False)
            parent_instance = CustomUser.objects.get(id=request.user.id)
            my_instance.user_id = parent_instance
            # my_instance.category_id = advert_form.cleaned_data['category']
            my_instance.save()  # Saves the data to the database

            return redirect('/')
        # else:
        #     print('nnnnnnnnnnnnnnnnnnnnnnnnnn')

    else:
        advert_form = AdvertForm()

    return render(request, "advert/advert.html", {'advert_form': advert_form})


def advert_edit(request):
    for key, value in request.GET.items():
        print(f"Parameter: {key}, Value: {value}")
    id_ad = request.GET.get('q',None)
    print(f'fsdfdsf - {id_ad}')
    advert_edit = Advert.objects.get_queryset_by_id(1)
    print(advert_edit.user_id)

    # advert_edit = Advert.objects.all()
    # for card in advert_edit:
    #     print(card.id)

    ad = Advert.objects.get(id=1)
    print(ad.category_id)

    # context = {'ad_db': ad_db}
    # return render(request, 'index.html', context=context)
    advert_form = AdvertForm()
    return render(request, "advert/advert.html", {'advert_form': advert_form})



def account(request):
    return TemplateResponse(request, "accounts/profile.html")


def exchange(request):
    return TemplateResponse(request, "advert/exchange.html")
