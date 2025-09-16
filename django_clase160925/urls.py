"""
URL configuration for django_clase160925 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from core import views as views_core

# Se importa el módulo de vistas de la app "core" con un alias (views_core).
# Esto se hace porque el proyecto tendrá más de una aplicación (por ejemplo, "foro" y "core"),
# y ambas contendrán un archivo views.py. Usar un alias evita ambigüedades al momento
# de referirse a sus funciones o clases.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_core.index,name="index"),

]
