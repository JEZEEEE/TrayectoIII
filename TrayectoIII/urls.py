from django.contrib import admin
from django.urls import path, include
from sistema import views as sistema_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sistema_views.login_view, name='login'),
    path('sistema/', include('sistema.urls')),
    path('productos/', include('productos.urls')),
    path('personas/', include('personas.urls'))
]
