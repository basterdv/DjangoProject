from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

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


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        # fields = '__all__'
        fields = [
            'title',
            'category_id',
            'description',
            'conditions'
        ]

    # def save(self,commit=True, user_id=None):
    #     instance = super().save(commit=False)  # Get the instance without saving yet
    #
    #     if user_id:
    #         print(user_id)
    #         instance.user = user_id  # Assign the user to the instance before saving
    #         print(instance.user)
    #     if commit:
    #         instance.save()
    #
    #     return instance


class ExchangeProposalForm(CustomUser):
    pass
