from django import forms

from goods.models import Advert
from users.models import CustomUser



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
    # category_id = forms.IntegerField()
    # description = forms.CharField()
    # conditions = forms.CharField()


class ExchangeProposalForm(CustomUser):
    pass
