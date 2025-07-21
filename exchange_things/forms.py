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
            # 'user_id'
            'title',
            'category_id',
            'description',
            'conditions',
            'image',
        ]

    # image = forms.ImageField(required=False)
    # title = forms.CharField()
    # # category_id = forms.IntegerField()
    # description = forms.CharField()
    # conditions = forms.CharField()



class ExchangeProposalForm(CustomUser):
    pass
