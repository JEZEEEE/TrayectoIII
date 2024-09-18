from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView
from .models import Persona
from .forms import PersonaForm

# criacion de las views personas

# def listar_personas(request):
#     personas = Persona.objects.all()
#     return render(request, 'personas/personas_list.html', {'personas': personas})
def listar_personas(request):
    tipo_persona = request.GET.get('tipo_persona')
    
    # Diccionario para mapear nombres a códigos
    tipo_persona_dict = {
        'cliente': 1,    # Supongamos que 1 es el código para 'cliente'
        'proveedor': 2,  # Supongamos que 2 es el código para 'proveedor'
    }
    
    if tipo_persona in tipo_persona_dict:
        personas = Persona.objects.filter(fky_tip_per=tipo_persona_dict[tipo_persona])
    else:
        personas = Persona.objects.all()

    return render(request, 'personas/personas_list.html', {'personas': personas})


def personas_update_form(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid(): 
            form.save()
        return redirect('personas_list')
    # Redirige a la lista de personas
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'personas/personasUpdate_form.html', {'form': form})  # Renderiza el formulario


def personas_update_form(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid(): 
            form.save()
        return redirect('personas_list')
    # Redirige a la lista de personas
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'personas/personasUpdate_form.html', {'form': form})  # Renderiza el formulario


def personas_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == 'GET':
        persona.est_per = 'I'  # Actualizamos el campo activo a False
        persona.save()
        return redirect('personas_list')  # Redirige a la lista de personas

    # Si es un GET, mostramos un formulario de confirmación (opcional)
    return render(request, 'personas/personas_list.html', {'persona': persona})



def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personas_list')
    else:
        form = PersonaForm()
    return render(request, 'personas/persona_form.html', {'form': form})