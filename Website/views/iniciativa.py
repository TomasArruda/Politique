from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Iniciativa
from Website.forms import IniciativaForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

def IniciativaView(request):
    query = Iniciativa.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

@login_required(login_url='/Website')
def CadastrarIniciativaView(request):

	form = IniciativaForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'cadastrarIniciativa.html', { "form" : form })

def EditarIniciativaView(request):
	return render(request, 'editarIniciativa.html')

@login_required(login_url='/Website')
def ConsultarIniciativaView(request):
	#iniciativas = Iniciativa.objects.filter().order_by('nome')
	iniciativas = serializers.serialize( "python", Iniciativa.objects.filter().order_by('nome') )
	return render(request, 'consultarIniciativa.html', {'iniciativas': iniciativas})

def RemoverIniciativaView(request, id):
	obj = Iniciativa.objects.get(pk=id)
	obj.delete()
	return render(request, 'consultarIniciativa.html')
