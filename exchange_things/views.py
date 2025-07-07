from django.db.utils import OperationalError
from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Ad

def custom_404_view(request, *args, **kwargs):
    return TemplateResponse(request, '404.html',status=404)
def index(request):
    try:
        ad_db = Ad.objects.all()
        # for card in ad_db:
        #     print(f'{card.id}: {card.title}')

        context = {'ad_db': ad_db}
        return render(request, 'index.html',context=context)
    except Ad.DoesNotExist:
        return TemplateResponse(request, '404.html')
    except OperationalError:
        return TemplateResponse(request, '404.html')




def sign_in(request):
    return TemplateResponse(request, "sing-in.html")


def register(request):
    return TemplateResponse(request, "register.html")


def ad(request):
    return TemplateResponse(request, "ad.html")


def account(request):
    return TemplateResponse(request, "account.html")


def exchange(request):
    return TemplateResponse(request, "exchange.html")
