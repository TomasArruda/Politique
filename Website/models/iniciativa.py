from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os
from customuser import CustomUser

class Iniciativa(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	data = models.DateField(auto_now=False, null=False, blank=False)

	tipoMembro = models.CharField(max_length=100, blank=False, default='', null=False)
	publicoAlvo = models.CharField(max_length=100, blank=False, default='', null=False)
	duracao = models.CharField(max_length=100, blank=False, default='', null=False)
	questoesChaves = models.CharField(max_length=500, blank=False, default='', null=False)
	areaAtuacao = models.CharField(max_length=100, blank=False, default='', null=False)
	missao = models.CharField(max_length=150, blank=False, default='', null=False)
	anoFundacao = models.IntegerField(default=0)
	website = models.CharField(max_length=100, blank=False, default='', null=False)
	parceiros = models.CharField(max_length=500, blank=False, default='', null=False)
	principaisProgramas = models.CharField(max_length=500, blank=False, default='', null=False)
	apoio = models.CharField(max_length=100, blank=False, default='', null=False)
	realizada = models.BooleanField(default=True)
	percepcaoPresenca = models.CharField(max_length=100, blank=False, default='', null=False)
	contato = models.CharField(max_length=100, blank=False, default='', null=False)

	#membro = models.ForeignKey(CustomUser,default='', null=True, blank = False)

	class  Meta:
		ordering = ('nome',)