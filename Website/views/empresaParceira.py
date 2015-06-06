from django.http import HttpResponse
from django.shortcuts import render
from Website.models import EmpresaParceira


def EmpresaParceiraView(request):
    query = EmpresaParceira.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarEmpresaView(request):
	return render(request, 'cadastrarEmpresa.html')