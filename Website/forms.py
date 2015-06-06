from Website.models import CustomUser
from django import forms

class CustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		exclude = ('last_login','eventos', 'date_joined')
