from venv import logger

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .forms import *
from .models import Libro, User, Copia
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


def gestione_home(request):
    return render(request, 'gestione/home.html')

class LibroListView(ListView):
    model = Libro
    title = "La nostra biblioteca possiede"
    template_name = 'gestione/lista_libri.html'


def search(request):
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get('search_string')
            where = form.cleaned_data.get('search_where')
            return redirect("gestione:ricerca_risultati", sstring, where)
    else:
        form = SearchForm()

    return render(request, template_name="gestione/ricerca.html", context={"form": form})

class LibroRicercaView(LibroListView):
    title = "La tua ricerca ha dato come risultato"

    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs['sstring']
        where = self.request.resolver_match.kwargs['where']

        if "Title" in where:
            qq = self.model.objects.filter(titolo__icontains=sstring)
        else:
            qq = self.model.objects.filter(autore__icontains=sstring)
        return qq





@login_required
def prestito(request, pk):
    User = get_user_model()
    #user = User.objects.get(pk=request.user.pk)
    libro = Libro.objects.get(pk=pk)
    copia_disponibile = libro.copie.filter(data_prestito=None).first()
    error_message = None

    if copia_disponibile:
        copia_disponibile.data_prestito = timezone.now()

        if request.user.is_authenticated:
            try:
                user = User.objects.get(pk=request.user.pk)

                if user.copie_in_prestito.filter(libro=libro).exists():
                    error_message = "Hai già preso in prestito una copia di questo libro"
                else:
                    copia_disponibile.utente = user
                    print('Copia assegnata all utente')
                    copia_disponibile.save()
            except User.DoesNotExist:
                print('Utente non trovato')
                return HttpResponse("User does not exist", status=404)
        else:
            print('Utente non autenticato')
            return HttpResponse("User not authenticated", status=403)

    if error_message is not None:
        libro = Libro
        return render(request, 'gestione/lista_libri.html', context={"Libro":libro, "error_message": error_message})

    return render(request, 'gestione/prestito.html', context={"libro": libro, "copia": copia_disponibile})


@login_required
def my_situation(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except User.DoesNotExist:
        return HttpResponseNotFound("User does not exist")
    copie = user.copie_in_prestito.all()
    ctx = {"listacopie":copie}
    return render(request, "gestione/situation.html", ctx)


class RestituisciView(LoginRequiredMixin, DetailView):
    model = Copia
    template_name = 'gestione/restituzione.html'
    errore = "NO_ERRORS"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        c = ctx["object"]

        if c.data_prestito != None:
            if c.utente.pk != self.request.user.pk:
                self.errore = "Non puoi restituire un libro che non hai preso in prestito"
            else:
                self.errore = "Libro attualmente non in prestito"

        if self.errore == "NO_ERRORS":
            try:
                c.data_prestito = None
                c.utente = None
                c.save()
            except Exception as e:
                print('Errore '+str(e))
                self.errore = 'Errore nella restituzione'

        return ctx

def get_hint(request):
    response = request.GET["q"]

    if(request.GET["w"] == 'Titolo'):
        q = Libro.objects.filter(titolo__icontains=response)
        if len(q) > 0:
            response = q[0].titolo
        else:
            q = Libro.objects.filter(autore__icontains=response)
            if len(q) > 0:
                response = q[0].autore

    return HttpResponse(response)