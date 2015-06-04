from django.shortcuts import render
from django.http import HttpResponse

def perfilView(request):
	return render(request, 'perfil.html')