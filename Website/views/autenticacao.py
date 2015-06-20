from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/Website')

def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/Website/Perfil')
        else:
            return HttpResponseRedirect('/Website')
    else:
        return HttpResponseRedirect('/Website')