from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor
from Website.forms import CustomUserForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Website')
def cadastrarMembroView(request):

    user_form = CustomUserForm(request.POST or None)

    # CONFERIR SETOR E SETAR PERMISSOES DE ACORDO COM SETOR

    if user_form.is_valid():
        user_form.save()

    return render(request, 'cadastrarmembro.html', {"form": user_form})

@login_required(login_url='/Website')
def ConsultarMembroView(request):
	membros = CustomUser.objects.filter().order_by('username')
	return render(request, 'consultarMembro.html', {'membros': membros})

def RemoverMembroView(request, id):
    obj = CystomUser.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarMembro.html')