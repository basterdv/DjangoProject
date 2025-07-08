from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from .models import CustomUser, Ad


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class AdForm(forms.Form):
    class Meta:
        model = Ad
        fields = [
            'title',
            'category_id',
            'user_id',
            'description',
            'conditions'
        ]


class ExchangeProposalForm(CustomUser):
    pass
