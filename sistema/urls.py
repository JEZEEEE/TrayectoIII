from django.urls import path
from .views import login_view, home, registro, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
]