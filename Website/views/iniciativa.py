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

@login_required(login_url='/Website')
def EditarIniciativaView(request, id):

	form = IniciativaForm(request.POST or None)
	obj = Iniciativa.objects.get(pk=id)

	if form.is_valid():
		obj.nome = form.cleaned_data['nome'] 
		obj.data = form.cleaned_data['data']
		obj.tipoMembro = form.cleaned_data['tipoMembro']
		obj.publicoAlvo = form.cleaned_data['publicoAlvo']
		obj.duracao = form.cleaned_data['duracao'] 
		obj.questoesChaves = form.cleaned_data['questoesChaves']
		obj.areaAtuacao = form.cleaned_data['areaAtuacao']
		obj.missao = form.cleaned_data['missao']
		obj.anoFundacao =  form.cleaned_data['anoFundacao']
		obj.website = form.cleaned_data['website']
		obj.parceiros = form.cleaned_data['parceiros']
		obj.principaisProgramas = form.cleaned_data['principaisProgramas']
		obj.apoio = form.cleaned_data['apoio']
		obj.realizada = form.cleaned_data['realizada']
		obj.percepcaoPresenca = form.cleaned_data['percepcaoPresenca']
		obj.contato = form.cleaned_data['contato']
		obj.membro = form.cleaned_data['membro']
		obj.save()

	iniciativas = serializers.serialize( "python", Iniciativa.objects.filter().order_by('nome') )
	return render(request, 'consultarIniciativa.html', {'iniciativas': iniciativas, 'form': form})

@login_required(login_url='/Website')
def ConsultarIniciativaView(request):
	form = IniciativaForm(None)
	# nome, data, duracao
	iniciativas = serializers.serialize( "python", Iniciativa.objects.filter().order_by('nome') )
	return render(request, 'consultarIniciativa.html', {'iniciativas': iniciativas, 'form': form})

@login_required(login_url='/Website')
def RemoverIniciativaView(request, id):	
	obj = Iniciativa.objects.get(pk=id)
	obj.delete()
	return render(request, 'consultarIniciativa.html')
