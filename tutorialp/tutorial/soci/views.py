from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Persona


class PersonaList(ListView):
    model = Persona
    template_name = 'soci/persona_list.html'

class PersoneDetail(DetailView):
    model = Persona
    template_name = 'soci/persona_detail.html' 


def home_page(request):
    return HttpResponse('Benvenuto nella pagina dei soci!')
