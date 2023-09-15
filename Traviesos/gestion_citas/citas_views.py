from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormAgendarCita, informacion_mascota
from django.contrib.auth.decorators import login_required
from .models import Mascota, AgendarCita

@login_required
def formulario_agendar(request):
    if request.method == 'POST':
        form = FormAgendarCita(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita guardada correctamente.')
            form = FormAgendarCita()
        else:
            messages.error(request, 'Error al agendar la cita. Revise los datos.')
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = FormAgendarCita()

    context = {'form': form}
    return render(request, 'citas/citas.html', context)


def datos_mascota(request):
    if request.method == 'POST':
        formulario2 = informacion_mascota(request.POST)
        if formulario2.is_valid():
            informacion_mascotas = formulario2.save(commit=False)
            informacion_mascotas.user = request.user
            informacion_mascotas.save()
            messages.success(request, 'Tu información adicional se ha guardado correctamente.')
            return redirect('mascota') 
    
    else:
        formulario2 = informacion_mascota()
    return render(request, 'citas/datos_mascotas.html', {'formulario': formulario2})

def agregar_mascota(request):
    lista = Mascota.objects.all()
    print(lista)
    return render(request, 'citas/mascota.html', {'lista': lista})

def ver_citas(request):
    citas = AgendarCita.objects.all()
    print(citas)
    return render(request, 'citas/lista_citas.html', {'citas': citas})
    
