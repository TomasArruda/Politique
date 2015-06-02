from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *

class Membro(models.Model):
	user = models.OneToOneField(User)
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	email = models.EmailField(blank=False, null=False, default='')
	
	eventos = models.ManyToManyField('Evento')
	setor = models.ForeignKey('Setor',default='')

	class  Meta:
		ordering = ('nome',)