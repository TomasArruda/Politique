from django.contrib.auth.models import User
from django import forms
from Website.models import Membro

class MembroForm(forms.Form):
	nome = forms.CharField()
	email = forms.CharField()
	password = forms.CharField()
	telefone = forms.CharField()
	setor = forms.CharField()
