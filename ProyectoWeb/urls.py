"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #de este modo tengo que anteponer 'ProyectoWebApp para acceder a los otros links
    #path('ProyectoWebApp/',include('ProyectoWebApp.urls')),
    #mientras que con esta forma no es necesario anteponer nada
    path('servicios/', include('Servicios.urls')),
    path('blog/', include('Blog.urls')),
    path('contacto/',include('Contacto.urls')),
    path('tienda/',include('Tienda.urls')),
    path('carro/',include('Carro.urls')),
    path('autenticacion/',include('Autenticacion.urls')),
    path('pedidos/',include('Pedidos.urls')),
    path('',include('ProyectoWebApp.urls')),
]

