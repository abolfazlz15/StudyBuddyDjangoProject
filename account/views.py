from django.contrib.auth import login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from .forms import LoginForm
from .models import User


class UserProfileView(DetailView):
    model= User
    template_name = 'account/profile.html'
    


class UserLoginView(generic.FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:home')
        
    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.get(email=data['email'])
        login(self.request, user)
        return super().form_valid(form)
