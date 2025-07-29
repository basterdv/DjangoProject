from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField()
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#
#     USERNAME_FIELD = 'email'

class CustomUser(AbstractUser):

    user = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = MyUserManager()

    def __str__(self):
        return self.email