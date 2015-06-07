from Website.models import EmpresaParceira
from django import forms

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = EmpresaParceira
		exclude = ('tipoParceria','iniciativas',)