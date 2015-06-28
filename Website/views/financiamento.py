from django.http import HttpResponse
from Website.forms import FinanciamentoForm
from Website.models import Financiamento
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required

def FinanciamentoView(request):
    query = Financiamento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

@login_required(login_url='/Website')
def CadastrarFinanciamentoView(request):

	form = FinanciamentoForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'cadastrarFinanciamento.html', { "form" : form })

@login_required(login_url='/Website')
def EditarFinanciamentoView(request, id):
	form = FinanciamentoForm(request.POST or None)
	obj = Financiamento.objects.get(pk=id)

	if form.is_valid():
		obj.nome = form.cleaned_data['nome'] 
		obj.processo = form.cleaned_data['processo']
		obj.tema = form.cleaned_data['tema']
		obj.projetos = form.cleaned_data['projetos']
		obj.valor = form.cleaned_data['valor'] 
		obj.prazos = form.cleaned_data['prazos']
		obj.instituicaoResponsavel = form.cleaned_data['instituicaoResponsavel']
		obj.vencedoresAnteriores = form.cleaned_data['vencedoresAnteriores']
		obj.membro = form.cleaned_data['membro']
		obj.save()

	financiamentos = serializers.serialize( "python", Financiamento.objects.filter().order_by('nome') )
	return render(request, 'consultarFinanciamento.html', {'financiamentos': financiamentos, 'form': form})

@login_required(login_url='/Website')
def ConsultarFinanciamentoView(request):
	form = FinanciamentoForm(None)
	financiamentos = serializers.serialize( "python", Financiamento.objects.filter().order_by('nome') )
	return render(request, 'consultarFinanciamento.html', {'financiamentos': financiamentos, 'form' : form})

@login_required(login_url='/Website')
def RemoverFinanciamentoView(request, id):
	obj = Financiamento.objects.get(pk=id)
	obj.delete()
	form = FinanciamentoForm(request.POST or None)
	financiamentos = serializers.serialize( "python", Financiamento.objects.filter().order_by('nome') )
	return render(request, 'consultarFinanciamento.html', {'financiamentos': financiamentos, 'form': form})
