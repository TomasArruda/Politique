from django.http import HttpResponse

from Website.models import Setor


def SetorView(request):
    query = Setor.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)