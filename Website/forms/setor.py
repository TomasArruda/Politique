from Website.models import Setor
from django import forms

class SetorForm(forms.ModelForm):
	class Meta:
		model = Setor
		exclude = ()