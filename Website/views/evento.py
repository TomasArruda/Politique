from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Evento

def EventoView(request):
    query = Evento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarEventoView(request):
	return render(request, 'cadastrarEvento.html')