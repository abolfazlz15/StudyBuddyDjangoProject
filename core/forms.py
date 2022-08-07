from django import forms
from .models import Message
from django.forms import ValidationError, TextInput

class MessageFrom(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        widgets = {
                'text': TextInput(attrs={'class':'room__message', 'placeholder': 'Write Your Message'})
        }