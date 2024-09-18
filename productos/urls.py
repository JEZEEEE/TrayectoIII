from django.urls import path
from . import views

urlpatterns = [
    # URLs para productos
    path('', views.listar_productos, name='listar_productos'),
    path('nuevo/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # URLs para categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),

    # URLs para marcas
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/nueva/', views.crear_marca, name='crear_marca'),
    path('marcas/editar/<int:pk>/', views.editar_marca, name='editar_marca'),
    path('marcas/eliminar/<int:pk>/', views.eliminar_marca, name='eliminar_marca'),
    
    path('generar-pdf/', views.generar_pdf_productos, name='generar_pdf_productos'),
]
