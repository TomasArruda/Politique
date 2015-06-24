from Website.models import Financiamento
from django import forms

class FinanciamentoForm(forms.ModelForm):

	class Meta:
		model = Financiamento
		exclude = ()