from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Membro
from Website.forms import MembroForm

def cadastrarMembroView(request):
    if request.method == 'POST':
        membro_form = MembroForm(request.POST)

        if membro_form.is_valid():
            nome = membro_form.cleaned_data["nome"]
            email = membro_form.cleaned_data["email"]
            senha = membro_form.cleaned_data["senha"]
            telefone = membro_form.cleaned_data["senha"]
            setor = membro_form.cleaned_data["senha"]

            membro = Membro(nome=nome, email = email, senha = senha, telefone = telefone, setor = setor)
            #membro.set_password(membro.password)
            membro.save()

        # profile = membro_form.save(commit=False)
        # profile.membro = membro

        # profile.save()
        else:
            print membro_form.errors
    else:
        membro_form = MembroForm()
    return render(request, 'cadastrarmembro.html', {"form": membro_form})

