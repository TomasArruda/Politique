from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor
from Website.forms import SetorForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

def SetorView(request):
	setores = serializers.serialize( "python", Setor.objects.filter().order_by('nome'), fields=('nome') )
	return render(request, 'setores.html', {'setores': setores})
    #query = Setor.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #return render(request, 'setores.html')

@login_required(login_url='/Website')
def CadastrarSetorView(request):
	form = SetorForm(request.POST or None)

	if form.is_valid():
		form.save()
		
	return render(request, 'setores.html', {"form":form})

@login_required(login_url='/Website')
def RemoverSetorView(request):

	return render(request, 'setores.html')
