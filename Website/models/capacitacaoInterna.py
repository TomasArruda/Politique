from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
from Website.models import Evento
import binascii
import os

class CapacitacaoInterna(Evento):
	material = models.CharField(max_length=200, blank=False, default='', null=False)

	def __str__(self):
		return self.nome
