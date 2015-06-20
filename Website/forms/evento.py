from Website.models import EventoInstitucional
from Website.models import CapacitacaoInterna
from Website.models import CapacitacaoExterna
from Website.models import Evento
from django import forms

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		exclude = ()

class EventoInstitucionalForm(forms.ModelForm):
	class Meta:
		model = EventoInstitucional
		exclude = ('empresasParceiras',)

class CapacitacaoInternaForm(forms.ModelForm):
	class Meta:
		model = CapacitacaoInterna
		exclude = ()

class CapacitacaoExternaForm(forms.ModelForm):
	class Meta:
		model = CapacitacaoExterna
		exclude = ()
