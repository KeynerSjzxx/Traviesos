from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'index.html')

@login_required
def perfil (request):
    return render(request, 'login/perfil.html', {'user': request.user})

def crear_cuenta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            return redirect('index')  # Redirige al usuario después del registro
    else:
        form = UserCreationForm()
    return render(request, 'login/registro.html', {'form': form})
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login/login.html',{

    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('index')    