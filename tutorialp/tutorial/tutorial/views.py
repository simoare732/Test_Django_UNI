from django.http import HttpResponse

from datetime import datetime

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def home_page(request):
    
    response = "Ciao <br> bello"

    return HttpResponse(response)


def elenca_params(request):

    response = ""

    for k in request.GET:
        response += request.GET[k] + " "

    return HttpResponse(response)

def welcome_home(request, nome, eta):

    return HttpResponse("Si chiama "+nome+" ed ha "+str(eta)+" anni")


def hello_template(request):
    ctx = {"title":"Hello templates", "lista": [datetime.now(), datetime.today().strftime('%A'), datetime.today().strftime('%B')]}

    return render(request, template_name="baseext.html", context=ctx)


def hello_params(request, nome):

    cont = {
        'nome':nome
    }
    
    return render(request, template_name="basepar.html", context=cont)


def page_with_static(request):
    return render(request, template_name="pwstatic.html", context={'title':"Pagina con elementi statici"})