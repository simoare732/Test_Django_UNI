"""
URL configuration for biblio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home_page, name='Home page'),
    path('libri/', views.LibriList.as_view(), name="libri"),
    path('listalibri/', views.lista_libri, name="listalibri"),
    path('listalibriF/', views.mattoni, name="listaFiltrata"),
    path('crealibro/', views.crea_libro, name='crealibro'),
    path('eliminalibro/', views.elimina_libro, name='eliminalibro'),
    path('modificalibro/<str:titolo>/<str:autore>/', views.modifica_libro, name='modificalibro'),

]
