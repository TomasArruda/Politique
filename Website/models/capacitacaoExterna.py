from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
from Website.models import Evento
import binascii
import os

class CapacitacaoExterna(Evento):
	custo = models.CharField(max_length=100, blank=False, default='', null=False)
	palestrante = models.CharField(max_length=100, blank=False, default='', null=False)
