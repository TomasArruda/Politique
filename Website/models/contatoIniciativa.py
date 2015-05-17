from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class ContatoIniciativa(models.Model):
	contatos = models.CharField(max_length=500, blank=False, default='', null=False)

	iniciativa = models.ForeignKey('Iniciativa',default='', null=False, blank = False)
	
	class  Meta:
		ordering = ('id',)