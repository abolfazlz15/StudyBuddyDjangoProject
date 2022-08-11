from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    profile_image = models.ImageField(upload_to='user_profile', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

