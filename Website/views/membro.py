from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Membro


def MembroView(request):
    membros = Membro.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def cadastrarMembroView(request):
	return render(request, 'cadastrarmembro.html')
