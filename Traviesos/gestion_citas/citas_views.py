from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormAgendarCita, informacion_mascota
from django.contrib.auth.decorators import login_required

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

@login_required
def datos_mascota(request):
    if request.method == 'POST':
        formulario = informacion_mascota(request.POST)
        if formulario.is_valid():
            informacion_mascotas = formulario.save(commit=False)
            informacion_mascotas.user = request.user
            informacion_mascotas.save()
            messages.success(request, 'Tu información adicional se ha guardado correctamente.')
            return redirect('mascota') 
    
    else:
        formulario = informacion_mascota()
    return render(request, 'citas/datos_mascotas.html', {'formulario': formulario})

def agregar_mascota(request):
    return render(request, 'citas/mascota.html')
    
