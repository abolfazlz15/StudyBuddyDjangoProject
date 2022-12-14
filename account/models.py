from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='user_profile', null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.is_admin

    def showImage(self):
        if self.avatar:
            return format_html(f'<img src="{self.avatar.url}" alt="" width="50px" height="50px">')
        else:
            return format_html('No Profile')

    showImage.short_description = 'Profile Image'      
