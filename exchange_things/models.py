from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models



class CustomUser(AbstractUser):
    pass
    # username = None
    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    #
    # # objects = MyUserManager()
    #
    # def __str__(self):
    #     return self.email

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField()
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#
#     USERNAME_FIELD = 'email'

class Category(models.Model):
    """ Категории объявлений """
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории',max_length=128,unique=True)
    # slug = models.SlugField(max_length=128, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = "categories"  # Correct pluralization in admin

    def __str__(self):
        return self.name

class Advert(models.Model):
    """ Объявления """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('CustomUser', null=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)
    title = models.CharField("Заголовок",max_length=350)
    description = models.TextField('Описание',null=True)
    image = models.ImageField("Картинка", null=True)
    conditions = models.BooleanField('Состояние',default=0)
    created_at = models.DateTimeField('Дата создания',auto_now_add=True)

class ExchangeProposal(models.Model):
    """ Обмен   """
    # status choice
    ChoiceField = (
        ('1','ожидает'),
        ('2','принята'),
        ('3','отклонена')
    )
    id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey('Advert', null=False,on_delete=models.CASCADE,related_name='sender_id')
    receiver_id = models.ForeignKey('Advert',null=False, on_delete=models.CASCADE,related_name='receiver_id')
    comment = models.TextField('Комментарий к сделки')
    created_at = models.DateTimeField('Дата создания сделки',auto_now_add=True)
    status = models.CharField('Статус сделки',max_length=300, choices=ChoiceField)
