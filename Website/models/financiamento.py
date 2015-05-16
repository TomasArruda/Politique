from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Financiamento(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	processo = models.CharField(max_length=100, blank=False, default='', null=False)
	tema = models.CharField(max_length=100, blank=False, default='', null=False)
	projetos = models.CharField(max_length=100, blank=False, default='', null=False)
	valor = models.CharField(max_length=100, blank=False, default='', null=False)
	prazos = models.CharField(max_length=100, blank=False, default='', null=False)
	instituicaoResponsavel = models.CharField(max_length=100, blank=False, default='', null=False)
	vencedoresAnteriores = models.CharField(max_length=500, blank=False, default='', null=False)

	membro = models.ForeignKey('Membro',default='', null=False, blank = False)

	class  Meta:
		ordering = ('nome',)