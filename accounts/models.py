import secrets

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def create_user(self, *args, **kwargs):
        u = super().create_user(*args, **kwargs)
        u.new_api_key()
        return u

    def create_superuser(self, *args, **kwargs):
        kwargs.setdefault('email', 'none@mail.ru')
        return super().create_superuser(*args, **kwargs)


class CustomUser(AbstractUser):
    """Using for next extension the user model"""
    username = models.CharField(max_length=30, unique=True,)
    api_key = models.CharField(max_length=16)
    email = models.CharField(max_length=100, default=None, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def new_api_key(self):
        self.api_key = secrets.token_urlsafe(12)