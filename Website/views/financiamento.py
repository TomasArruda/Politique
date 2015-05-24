from django.http import HttpResponse

from Website.models import Financiamento


def FinanciamentoView(request):
    query = Financiamento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)