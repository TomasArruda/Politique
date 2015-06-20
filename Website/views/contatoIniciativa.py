from django.http import HttpResponse

from Website.models import ContatoIniciativa


def ContatoIniciativaView(request):
    query = ContatoIniciativa.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)