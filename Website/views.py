from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def atualizarperfil(request):
    return render(request, 'atualizarperfil.html')
