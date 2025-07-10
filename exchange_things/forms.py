from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

from .models import CustomUser, Advert


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        # fields = '__all__'
        fields = [
            'title',
            'category_id',
            'description',
            'conditions',
            'image',
        ]



class ExchangeProposalForm(CustomUser):
    pass
