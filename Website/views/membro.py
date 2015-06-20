from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor, CustomUser
from Website.forms import CustomUserForm
from django.core import serializers

def cadastrarMembroView(request):

    user_form = CustomUserForm(request.POST or None)

    if user_form.is_valid():
        user_form.save()

    return render(request, 'cadastrarmembro.html', {"form": user_form})

def ConsultarMembroView(request):
	membros = serializers.serialize( "python", CustomUser.objects.filter().order_by('username') )
	return render(request, 'consultarMembro.html', {'membros': membros})
