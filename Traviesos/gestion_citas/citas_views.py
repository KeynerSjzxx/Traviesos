from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FormAgendarCita, informacion_mascota
from django.contrib.auth.decorators import login_required
from .models import Mascota, AgendarCita
from django.contrib.auth.models import User

@login_required
def formulario_agendar(request):
    if request.method == 'POST':
        form = FormAgendarCita(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita se ha enviado exitosamente.')
            form = FormAgendarCita()
        else:
            messages.error(request, 'Error al agendar cita. Verifica los datos.')

    else:
        form = FormAgendarCita()

    context = {'form': form}
    return render(request, 'citas/citas.html', context)

@login_required
def datos_mascota(request):
    if request.method == 'POST':
        formulario2 = informacion_mascota(request.POST)
        if formulario2.is_valid():
            informacion_mascotas = formulario2.save(commit=False)
            informacion_mascotas.user = request.user
            informacion_mascotas.save()
            return redirect('agregar_mascotas') 
    
    else:
        formulario2 = informacion_mascota()
    return render(request, 'citas/datos_mascotas.html', {'formulario': formulario2})

@login_required
def agregar_mascota(request):
    lista = Mascota.objects.filter(user=request.user)
    print(lista)
    return render(request, 'citas/mascota.html', {'lista': lista})

def ver_citas(request):
    citas = AgendarCita.objects.filter(Nombre__user=request.user)
    print(citas)
    return render(request, 'citas/lista_citas.html', {'citas': citas})

@login_required
def eliminar_mascota(request, mascota_id):
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, id=mascota_id, user=request.user)
        mascota.delete()
        return redirect('agregar_mascotas')
    
    return render(request, 'mascota.html', {'mascota': mascota})

@login_required
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id, user=request.user)
    
    if request.method == 'POST':
        formulario = informacion_mascota(request.POST, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            return redirect('agregar_mascotas')
    else:
        formulario = informacion_mascota(instance=mascota)
        
    return render(request, 'citas/datos_mascotas.html',{'formulario':formulario})

@login_required
def eliminar_cita(request, agendarCita_id):
    if request.method == 'POST':
        citas = get_object_or_404(AgendarCita, id=agendarCita_id, Nombre__user=request.user)
        citas.delete()
        return redirect('ver_citas')
    
    return render(request, 'mascota.html', {'citas': citas})

@login_required
def editar_cita(request, agendarCita_id):
    cita = get_object_or_404(AgendarCita, id=agendarCita_id, Nombre__user=request.user)
    
    if request.method == 'POST':
        formulario = FormAgendarCita(request.POST, instance=cita)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver_citas')
    else:
        formulario = FormAgendarCita(instance=cita)
        
    return render(request, 'citas/citas.html', {'formulario': formulario})
