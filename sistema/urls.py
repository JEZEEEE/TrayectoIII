from django.urls import path
from .views import login_view, home, registro, logout_view, listar_usuarios,eliminar_usuario,modificar_usuario_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('eliminar_usuario/<int:cod_usu>/', eliminar_usuario, name='eliminar_usuario'),
    path('modificar_usuario/<int:cod_usu>/', modificar_usuario_view, name='modificar_usuario'),
]