from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# class AccountManager(BaseUserManager):
#     def create_user(self, username, email, password, **extra_fields):
#         pass
#     def create_superuser(self, username, email, password, **extra_fields):
#         pass
#     def create_account(self, username, email, password, **extra_fields):
#         pass
#     def create_user_account(self, username, email, password, **extra_fields):
#         pass

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(null=True)
    conditions = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class ExchangeProposal(models.Model):
    # status choice
    ChoiceField = (
        ('1','ожидает'),
        ('2','принята'),
        ('3','отклонена')
    )
    id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey('Ad', null=False,on_delete=models.CASCADE,related_name='sender_id')
    receiver_id = models.ForeignKey('Ad',null=False, on_delete=models.CASCADE,related_name='receiver_id')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=300, choices=ChoiceField)
