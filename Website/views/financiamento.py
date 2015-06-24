from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Financiamento
from Website.forms import FinanciamentoForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

def FinanciamentoView(request):
    query = Financiamento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    render(request, 'cadastrarFinanciamento.html')

@login_required(login_url='/Website')
def CadastrarFinanciamentoView(request):

	form = FinanciamentoForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'cadastrarFinanciamento.html', { "form" : form })

def EditarFinanciamentoView(request):
	return render(request, 'editarFinanciamento.html')

@login_required(login_url='/Website')
def ConsultarFinanciamentoView(request):
	#iniciativas = Financiamento.objects.filter().order_by('nome')
	financiamentos = serializers.serialize( "python", Financiamento.objects.filter().order_by('nome') )
	return render(request, 'consultarFinanciamento.html', {'financiamentos': financiamentos})

def RemoverFinanciamentoView(request, id):
	obj = Financiamento.objects.get(pk=id)
	obj.delete()
	return render(request, 'consultarFinanciamento.html')