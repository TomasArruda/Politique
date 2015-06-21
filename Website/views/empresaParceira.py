from django.http import HttpResponse
from django.shortcuts import render
from Website.models import EmpresaParceira
from Website.forms import EmpresaForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

def EmpresaParceiraView(request):
    query = EmpresaParceira.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

@login_required(login_url='/Website')
def CadastrarEmpresaView(request):
	form = EmpresaForm(request.POST or None)

	if form.is_valid():
		form.save()
		
	return render(request, 'cadastrarEmpresa.html', { "form" : form })

@login_required(login_url='/Website')
def ConsultarEmpresaView(request):
	empresas = serializers.serialize( "python", EmpresaParceira.objects.filter().order_by('nome') )
	return render(request, 'consultarEmpresa.html', {'empresas': empresas})

def RemoverEmpresaView(request, id):
    obj = EmpresaParceira.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarEmpresa.html')
