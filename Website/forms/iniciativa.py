from Website.models import Iniciativa
from django import forms

class IniciativaForm(forms.ModelForm):

	realizada = forms.BooleanField(required=False)

	class Meta:
		model = Iniciativa
		exclude = ()