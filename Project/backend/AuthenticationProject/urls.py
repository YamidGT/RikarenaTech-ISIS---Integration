from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('allauth.urls')),            # Para rutas de allauth
    path('api/', include('AuthenticationProject.api_urls')),  # Para rutas de la app de autenticación
]