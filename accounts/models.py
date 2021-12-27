from django.contrib.auth.models import AbstractUser
from django.db import models
# from rest_framework_api_key.models import AbstractAPIKey


# class CustomUserManager(UserManager):
#     pass
#     def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not username:
#             raise ValueError('The given username must be set')
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         print('Creating API key...')
#         user.new_api_key()
#         print('API created!')
#         user.save(using=self._db)
#         return user


class CustomUser(AbstractUser):
    """Using for next extension the user model"""
    pass
#     username = models.CharField(max_length=30, unique=True,)
#     # api_key = models.CharField(max_length=64)

#     # objects = CustomUserManager()

#     USERNAME_FIELD = 'username'

#     # def new_api_key(self):
#     #     self.api_key = secrets.token_hex(32)

# class CustomUserAPIKey(AbstractAPIKey):
#     customuser = models.ForeignKey(
#         CustomUser,
#         on_delete=models.CASCADE,
#         related_name='api_keys',
#     )