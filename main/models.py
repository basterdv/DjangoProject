from django.db import models

from users.models import CustomUser
from goods.models import Advert



class ExchangeProposal(models.Model):
    """ Обмен   """
    # status choice
    ChoiceField = (
        ('1', 'ожидает'),
        ('2', 'принята'),
        ('3', 'отклонена')
    )
    id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(Advert, null=False, on_delete=models.CASCADE, related_name='sender_id')
    # sender_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(Advert, null=False, on_delete=models.CASCADE, related_name='receiver_id')
    comment = models.TextField('Комментарий к сделки')
    created_at = models.DateTimeField('Дата создания сделки', auto_now_add=True)
    status = models.CharField('Статус сделки', max_length=300, choices=ChoiceField)
