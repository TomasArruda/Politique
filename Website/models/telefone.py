from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os
from customuser import CustomUser

class Telefone(models.Model):
	telefone = PhoneNumberField(null=False, blank = False, unique = True)

	membro = models.ForeignKey(CustomUser,default='', null=False, blank = False)

	def __str__(self):
		return self.nome
	
	class  Meta:
		ordering = ('id',)