from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Iniciativa


def IniciativaView(request):
    query = Iniciativa.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarIniciativaView(request):
	return render(request, 'cadastrarIniciativa.html')

def EditarIniciativaView(request):
	return render(request, 'editarIniciativa.html')