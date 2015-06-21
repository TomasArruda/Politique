from Website.models import Evento, EventoInstitucional, CapacitacaoExterna, CapacitacaoInterna

from django import forms

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento

class EventoInstitucionalForm(forms.ModelForm):
	class Meta:
		model = EventoInstitucional

class CapacitacaoInternaForm(forms.ModelForm):
	class Meta:
		model = CapacitacaoInterna

class CapacitacaoExternaForm(forms.ModelForm):
	class Meta:
		model = CapacitacaoExterna
