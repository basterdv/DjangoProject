from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField()
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#
#     USERNAME_FIELD = 'email'

class CustomUser(AbstractUser):

    # user = None
    username = models.CharField(max_length=150,null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = MyUserManager()

    def __str__(self):
        return self.email