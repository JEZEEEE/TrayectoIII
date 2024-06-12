from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm, AsignarRolPermisosForm
from .models import Usuario
import logging
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            logging.debug("Formulario válido")
            form.save()
            logging.debug("Formulario guardado")
            return redirect('login')
        else:
            logging.debug("Formulario inválido")
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Usuario.objects.get(cor_usu=email, con_usu=password, est_usu='A')
                print(f"Usuario autenticado: {user}")  # Mensaje de depuración
                request.session['cod_usu'] = user.cod_usu # Clave Primaria de la tabla usuario 
                return redirect('home')
            except Usuario.DoesNotExist:
                print("Error de autenticación")  # Mensaje de depuración
                messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    cod_usu = request.session.get('cod_usu') # Para que reconozca que usuario es el que esta en sesion 
    if not cod_usu:
        return redirect('login')
    return render(request, 'home.html')

@login_required
def asignar_roles_permisos(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = AsignarRolPermisosForm(request.POST, usuario=usuario)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista_principal')
    else:
        form = AsignarRolPermisosForm(usuario=usuario)
    return render(request, 'asignar_roles_permisos.html', {'form': form, 'usuario': usuario})
