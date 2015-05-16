from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Evento(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	data = models.DateField(auto_now=False, null=False, blank=False)
	feedback = models.CharField(max_length=500, blank=False, default='', null=False)

	
	class  Meta:
		ordering = ('nome',)