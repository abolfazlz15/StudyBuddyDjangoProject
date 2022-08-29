from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from .models import User


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'phone_number', 'is_active', 'is_admin')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'enter your email'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'enter your password'})
    )

    def clean_password(self):
        user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('username or password is incorrect', code='invalid_info')