from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Website')
def perfilView(request):
	return render(request, 'perfil.html')