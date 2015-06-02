from django.http import HttpResponse

from Website.models import Telefone


def TelefoneView(request):
    query = Telefone.objects.order_by('membro')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    #render(request, '/membros.html', context)