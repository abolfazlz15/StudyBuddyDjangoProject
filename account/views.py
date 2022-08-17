from django.shortcuts import render
from django.views.generic import DetailView
from .models import User


class UserProfileView(DetailView):
    model= User
    template_name = 'account/profile.html'
    