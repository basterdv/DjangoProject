from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'index.html')


def sign_in(request):
    return TemplateResponse(request, "sing-in.html")


def register(request):
    return TemplateResponse(request, "register.html")
