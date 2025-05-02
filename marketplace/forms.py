from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from marketplace.models import Polso

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Polso
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Polso
        fields = ('username', 'email', 'adres', 'kontakt')