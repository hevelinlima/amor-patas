from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
  email = forms.EmailField(max_length=100)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

    