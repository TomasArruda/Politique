from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
from Website.models import Evento
import binascii
import os

class EventoInstitucional(Evento):
	custo = models.CharField(max_length=100, blank=False, default='', null=False)
	motivoPatrocinio = models.CharField(max_length=500, blank=False, default='', null=False)

	empresasParceiras = models.ManyToManyField('EmpresaParceira')

	def __str__(self):
		return self.nome