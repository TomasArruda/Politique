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
def ConsultarFinanciamentoView(request):
	#nome e valor
	financiamentos = serializers.serialize( "python", Financiamento.objects.filter().order_by('nome') )
	return render(request, 'consultarFinanciamento.html', {'financiamentos': financiamentos})

@login_required(login_url='/Website')
def RemoverFinanciamentoView(request, id):
    obj = Financiamento.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarFinanciamento.html')
