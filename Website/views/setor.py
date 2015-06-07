from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor
from Website.forms import SetorForm

def SetorView(request):
    query = Setor.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    return render(request, 'setores.html')

def CadastrarSetorView(request):

	form = SetorForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'setores.html', {"form":form})

def RemoverSetorView(request):

	return render(request, 'setores.html')

