from django.contrib import admin
from main.models import CustomUser,ExchangeProposal
from goods.models import Category,Advert
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)

