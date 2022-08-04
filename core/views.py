from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'abofazl'
        return context
