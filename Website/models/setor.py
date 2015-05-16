from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Setor(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	Permissao = models.CharField(max_length=150, blank=False, default='', null=False)

	class  Meta:
		ordering = ('nome',)