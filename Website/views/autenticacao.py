from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def LogoutView(request):
    logout(request)
    return redirect('/Website')

def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/Website/Perfil')
        else:
            x = 0
            # Return a 'disabled account' error message
    else:
        x = 0
        # Return an 'invalid login' error message.