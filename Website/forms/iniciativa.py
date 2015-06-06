from Website.models import Iniciativa
from django import forms

class IniciativaForm(forms.ModelForm):
	class Meta:
		model = Iniciativa
		exclude = ('membro',)