# from django.contrib.auth.models import User
# from django import forms
# from Website.models import CustomUser

# class CustomUserForm(forms.ModelForm):
# 	nome = forms.CharField()
# 	email = forms.CharField()
# 	password = forms.CharField()
# 	setor = forms.CharField()
# 	class Meta:
# 		model = CustomUser

from Website.models import CustomUser
from django import forms

class CustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		exclude = ('last_login','eventos', 'date_joined')

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(CustomUserForm, self).save(commit=False)
		user.is_active=True
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user
