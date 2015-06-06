from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Setor
from Website.forms import CustomUserForm

def cadastrarMembroView(request):

    user_form = CustomUserForm(request.POST or None)

    if user_form.is_valid():
        user_form.save()

    return render(request, 'cadastrarmembro.html', {"form": user_form})

