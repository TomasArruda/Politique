from django.http import HttpResponse

from Website.models import CapacitacaoInterna


def ContatoCapacitacaoView(request):
    query = ContatoCapacitacao.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)