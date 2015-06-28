from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor, CustomUser
from Website.forms import CustomUserForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Website')
def cadastrarMembroView(request):

    user_form = CustomUserForm(request.POST or None)

    # CONFERIR SETOR E SETAR PERMISSOES DE ACORDO COM SETOR

    if user_form.is_valid():
        user_form.save()

    return render(request, 'cadastrarmembro.html', {"form": user_form})

@login_required(login_url='/Website')
def EditarMembroView(request, id):

    form = CustomUserForm(request.POST or None)
    obj = CustomUser.objects.get(pk=id)

    if form.is_valid():
        obj.first_name = form.cleaned_data['first_name'] 
        obj.username = form.cleaned_data['username']
        obj.email = form.cleaned_data['email']
        obj.setor = form.cleaned_data['setor'] 
        obj.save()

    membros = serializers.serialize( "python", CustomUser.objects.filter().order_by('first_name'), fields=('username','first_name', 'setor') )
    return render(request, 'consultarMembro.html', {'membros': membros, 'form': form})


@login_required(login_url='/Website')
def AtualizarMembroView(request, id):
    obj = CustomUser.objects.get(pk=id)
    return render(request, 'consultarMembro.html')

@login_required(login_url='/Website')
def ConsultarMembroView(request):
    form = CustomUserForm(None)
    membros = serializers.serialize( "python", CustomUser.objects.filter().order_by('username'), fields=('username','first_name', 'setor') )
    return render(request, 'consultarMembro.html', {'membros': membros, 'form':form})

@login_required(login_url='/Website')
def RemoverMembroView(request, id):
    obj = CustomUser.objects.get(pk=id)
    obj.delete()
    form = CustomUserForm(None)
    membros = serializers.serialize( "python", CustomUser.objects.filter().order_by('username'), fields=('username','first_name', 'setor') )
    return render(request, 'consultarMembro.html', {'membros': membros, 'form':form})
