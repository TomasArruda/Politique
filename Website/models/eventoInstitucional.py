from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class EventoInstitucional(models.Model):
	custo = models.CharField(max_length=100, blank=False, default='', null=False)
	mostivoPatrocinio = models.CharField(max_length=500, blank=False, default='', null=False)

	empresasParceiras = models.ManyToManyField('EmpresaParceira')
	evento = models.ForeignKey('Evento',default='')
	
	class  Meta:
		ordering = ('evento',)