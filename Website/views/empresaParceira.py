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
def EditarEmpresaView(request, id):
	form = EmpresaForm(request.POST or None)
	obj = EmpresaParceira.objects.get(pk=id)

	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	ramoAtuacao = models.CharField(max_length=100, blank=False, default='', null=False)
	background = models.CharField(max_length=100, blank=False, default='', null=False)
	apoios = models.CharField(max_length=100, blank=False, default='', null=False)
	propostaApoio = models.CharField(max_length=100, blank=False, default='', null=False)

	tipoParceria = models.ForeignKey('TipoParceria',default='', null=True, blank = False)
	iniciativas = models.ManyToManyField('Iniciativa')

	if form.is_valid():
		obj.nome = form.cleaned_data['nome'] 
		obj.ramoAtuacao = form.cleaned_data['ramoAtuacao']
		obj.background = form.cleaned_data['background']
		obj.apoios = form.cleaned_data['apoios']
		obj.propostaApoio = form.cleaned_data['propostaApoio'] 
		obj.tipoParceria = form.cleaned_data['tipoParceria']
		obj.iniciativas = form.cleaned_data['iniciativas']
		obj.save()

	empresas = serializers.serialize( "python", EmpresaParceira.objects.filter().order_by('nome') )
	return render(request, 'consultarFianaciamento.html', {'empresas': empresas, 'form': form})

@login_required(login_url='/Website')
def ConsultarEmpresaView(request):
	#nome e ramo
	form = EmpresaForm(None)
	empresas = serializers.serialize( "python", EmpresaParceira.objects.filter().order_by('nome') )
	return render(request, 'consultarEmpresa.html', {'empresas': empresas, 'form' : form})

@login_required(login_url='/Website')
def RemoverEmpresaView(request, id):
    obj = EmpresaParceira.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarEmpresa.html')
