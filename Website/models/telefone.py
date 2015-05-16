from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Telefone(models.Model):
	telefone = PhoneNumberField(null=False, blank = False, unique = True)

	membro = models.ForeignKey('Membro',default='', null=False, blank = False)
	
	class  Meta:
		ordering = ('id',)