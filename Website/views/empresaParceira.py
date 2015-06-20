from django.http import HttpResponse
from django.shortcuts import render
from Website.models import EmpresaParceira
from Website.forms import EmpresaForm

def EmpresaParceiraView(request):
    query = EmpresaParceira.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)

def CadastrarEmpresaView(request):

	form = EmpresaForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'cadastrarEmpresa.html', { "form" : form })

def ConsultarEmpresaView(request):
	empresas = EmpresaParceira.objects.filter().order_by('nome')
	return render(request, 'consultarEmpresa.html', {'empresas': empresas})

def RemoverEmpresaView(request, id):
    obj = EmpresaParceira.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarEmpresa.html')