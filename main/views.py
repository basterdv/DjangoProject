from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.db.utils import OperationalError
from django.shortcuts import render, redirect, get_object_or_404

# from goods.models import Categories
# from goods.models import Advert
#
# from users.models import CustomUser

# def index(request):
#     return HttpResponse("Hello METANIT.COM")


def index(request):
    # try:
    context = {
        'title': 'Обменяй - Бартерная платформа для обмена вещами',
        'context': 'Обмен'
    }

    return render(request, 'main/index.html', context=context)


# except Advert.DoesNotExist:
#     return TemplateResponse(request, '404.html')
# except OperationalError:
#     return TemplateResponse(request, '404.html')


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Любой текст',
    }
    return render(request, 'main/about.html', context)


def custom_404_view(request, *args, **kwargs):
    return TemplateResponse(request, '404.html', status=404)
