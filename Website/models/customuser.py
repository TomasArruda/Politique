from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

	eventos = models.ManyToManyField('Evento')
	setor = models.ForeignKey('Setor',null=True)

	USERNAME_FIELD = 'username'
	
	def __str__(self):
		return self.nome
