from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm, AsignarRolPermisosForm, ModificarUsuarioForm
from .models import Usuario
import logging
from .queries import obtener_usuarios, eliminar_usuario_logicamente, modificar_usuario
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Usuario
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
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

def listar_usuarios(request):
    usuarios = obtener_usuarios()
    print(f"Usuarios obtenidos: {usuarios}")  # Para depuración
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

##def eliminar_usuario(request, cod_usu):
##    eliminar_usuario_logicamente(cod_usu)
##    messages.success(request, 'Usuario eliminado correctamente.')
##    return redirect('listar_usuarios')

def eliminar_usuario(request, cod_usu):
    eliminar_usuario_logicamente(cod_usu)
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('listar_usuarios')


def modificar_usuario_view(request, cod_usu):
    usuario = get_object_or_404(Usuario, cod_usu=cod_usu)
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            data = form.cleaned_data
            modificar_usuario(
                cod_usu,
                data['cor_usu'],
                data['con_usu'],
                data['fky_per'].cod_per,
                data['fky_rol'].cod_rol,
                data['est_usu']
            )
            return redirect('listar_usuarios')
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, 'modificar_usuario.html', {'form': form, 'usuario': usuario})



def listar_usuarios_pdf(request):
    # Obtener todos los usuarios de la base de datos
    Usuarios = Usuario.objects.all().values('cod_usu', 'cor_usu', 'est_usu')

    # Cargar la plantilla HTML
    template = get_template('usuarios_pdf.html')
    context = {'usuarios': Usuarios}
    
    # Renderizar la plantilla con los datos
    html = template.render(context)

    # Crear la respuesta en PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="usuarios.pdf"'

    # Generar el PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verificar si hubo errores
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    
    return response