from django.contrib.auth.models import User
from django import forms
from Website.models import Membro

class MembroForm(forms.ModelForm):
	nome = forms.CharField()
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())
	telefone = forms.CharField()
	setor = forms.CharField()
