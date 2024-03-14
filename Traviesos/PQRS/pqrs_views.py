from django.shortcuts import render
from django.contrib import messages
from .models import Tipo_pqrs
from .forms import FormAgendarPqrs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PQRS

def formulario_pqrs(request):
    return render(request, 'PQRS/form.html', context)

def mostrar_formulario(request):
    return render(request, 'PQRS/form.html')

@login_required
def pqrs(request):
    return render(request, 'PQRS/form.html')

@login_required
def perfil_pqrs(request):
    usuario = User.objects.get(username=request.user.username)
    pqrs_usuario = PQRS.objects.filter(Nombre=usuario)
    return render(request, 'PQRS/PQRS_cliente.html', {'usuario': usuario, 'pqrs_usuario': pqrs_usuario})