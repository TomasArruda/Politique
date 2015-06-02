from django.shortcuts import render
from django.http import HttpResponse

def atualizarPerfilView(request):
    return render(request, 'atualizarPerfil.html')