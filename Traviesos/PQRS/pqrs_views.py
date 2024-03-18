from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FormAgendarPqrs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PQRS, Tipo_pqrs, Estado

@login_required
def formulario_pqrs(request):
    context = {}
    return render(request, 'PQRS/form.html', context)

@login_required
def pqrs(request):
    context = {}
    if request.method == 'POST':
        form = FormAgendarPqrs(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'PQRS enviada correctamente')
            form = FormAgendarPqrs() 
        else:
            messages.error(request, 'Error al enviar. Verifica los datos.')
    else:
        form = FormAgendarPqrs()
        
    usuario = User.objects.get(username=request.user.username)
    pqrs_usuario = PQRS.objects.filter(Nombre=usuario)
    context = {'form': form, 'user': request.user, 'pqrs_usuario': pqrs_usuario}
    return render(request, 'PQRS/form.html', context)

@login_required
def editar_pqrs(request, PQRS_id):
    pqrs = get_object_or_404(PQRS, id=PQRS_id, Nombre=request.user)
    
    if request.method == 'POST':
        formulario = FormAgendarPqrs(request.POST, instance=pqrs)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil_pqrs')
    else:
        formulario = FormAgendarPqrs(instance=pqrs)
    return render(request, 'PQRS/form.html', {'form': formulario})

@login_required
def perfil_pqrs(request):
    usuario = User.objects.get(username=request.user.username)
    pqrs_usuario = PQRS.objects.filter(Nombre=usuario)
    return render(request, 'PQRS/PQRS_cliente.html', {'usuario': usuario, 'pqrs_usuario': pqrs_usuario})

def anular_pqrs(request, pk):
    pqrs = get_object_or_404(PQRS, id=pk)
    estado_anulado = Estado.objects.get(Estado_pqrs="Anulado")
    
    if request.method == 'POST':
        pqrs.Estado_pqrs = estado_anulado
        pqrs.save()
        return redirect('perfil_pqrs')
    
    return redirect('perfil_pqrs')
