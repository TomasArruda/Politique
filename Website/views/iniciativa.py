from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Iniciativa
from Website.forms import IniciativaForm


def IniciativaView(request):
    query = Iniciativa.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarIniciativaView(request):

	form = IniciativaForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'cadastrarIniciativa.html', { "form" : form })

def EditarIniciativaView(request):
	return render(request, 'editarIniciativa.html')
