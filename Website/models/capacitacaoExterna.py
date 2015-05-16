from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class CapacitacaoExterna(models.Model):
	custo = models.CharField(max_length=100, blank=False, default='', null=False)
	palestrante = models.CharField(max_length=100, blank=False, default='', null=False)

	evento = models.ForeignKey('Evento',default='')
	
	class  Meta:
		ordering = ('evento',)