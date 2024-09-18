from django.urls import path
from . import views

urlpatterns = [
    path('personas/',views.listar_personas, name='personas_list'),
    path('personas/crear/', views.crear_persona, name='persona_form'),
    path('personas/<int:pk>/update/', views.personas_update_form, name='personas_update'),
    path('personas/<int:pk>/delete/', views.personas_delete, name='personas_delete')
]
