from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor

def SetorView(request):
    query = Setor.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    return render(request, 'setores.html')