from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Membro
from Website.forms import MembroForm

def cadastrarMembroView(request):
	return render(request, 'cadastrarmembro.html')

def cadastrarMembro(request):
	registered = False

	if request.method == 'POST':
		membro_form = MembroForm(data=request.POST)

		if membro_form.is_valid():
			user.set_password(user.password)
			user.save()

			profile = membro_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True
		else:
			print membro_form.errors
	else:
		membro_form = MembroForm()



