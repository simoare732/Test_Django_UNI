from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models


def index(request):
    return HttpResponse("Benvenuto nelle iscrizioni")

class ListaStudentiView(ListView):
    model = models.Studente
    template_name = "iscrizioni/lista_studenti.html"
    extra_context = {'title':'Lista di studenti'}

class ListaInsegnamentiAttivi(ListView):
    model = models.Insegnamento
    template_name = "iscrizioni/insegnamenti_attivi.html"

    def get_queryset(self):
        return self.model.objects.exclude(studenti__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Insegnamenti attivi'
        return context


class ListaInsegnamentiView(ListView):
    model = models.Insegnamento
    template_name = "iscrizioni/lista_insegnamenti.html"
    extra_context = {'title':'Lista di insegnamenti e studenti'}


class ListaStudentiIscritti(ListView):
    model = models.Studente
    template_name = "iscrizioni/studenti_iscritti.html"

    def get_model_name(self):
        return self.model._meta.verbose_name_plural

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Lista studenti con iscrizione'
        return ctx

    def get_totale_iscrizioni(self):
        count = 0
        for i in models.Insegnamento.objects.all():
            count += i.studenti.all().count()

        return count

class CreateStudenteView(CreateView):
    model = models.Studente
    template_name = "iscrizioni/crea_studente.html"
    fields = '__all__' #['name', 'surname']
    success_url = reverse_lazy("iscrizioni:listastudenti")

class CreateInsegnamentoView(CreateView):
    model = models.Insegnamento
    template_name = "iscrizioni/crea_insegnamento.html"
    fields = '__all__'
    success_url = reverse_lazy("iscrizioni:listainsegnamenti")


class DetailInsegnamentoView(DetailView):
    model = models.Insegnamento
    template_name = "iscrizioni/insegnamento.html"

class UpdateInsegnamentoView(UpdateView):
    model = models.Insegnamento
    template_name = "iscrizioni/edit_insegnamento.html"
    fields = "__all__"

    def get_success_url(self):
        pk = self.get_context_data()["object"].pk
        return reverse("iscrizioni:insegnamento", kwargs={"pk": pk})

class DeleteEntitaView(DeleteView):
    template_name = "iscrizioni/cancella_entry.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        entita = 'Studente'
        if self.model == models.Insegnamento:
            entita = 'Insegnamento'
        ctx['entita'] = entita
        return ctx

    def get_success_url(self):
        if self.model == models.Studente:
            return reverse("iscrizioni:listastudenti")
        else:
            return reverse("iscrizioni:listainsegnamenti")

class DeleteStudenteView(DeleteEntitaView):
    model = models.Studente

class DeleteInsegnamentoView(DeleteEntitaView):
    model = models.Insegnamento


def cerca_studenti(request):
    if request.method == "GET":
        return render(request, template_name="iscrizioni/cerca_studenti.html")
    else:
        if len(request.POST["name"]) < 1:
            nome = "null"
        else: nome = request.POST["name"]
        if len(request.POST["surname"]) < 1:
            cognome="null"
        else: cognome = request.POST["surname"]
        return redirect("iscrizioni:studentecercato", name=nome, surname=cognome)

class FiltraStudente(ListView):
    model = models.Studente
    template_name = "iscrizioni/listastudenteinsegnamento.html"

    def get_queryset(self):
        try:
            arg = self.kwargs["name"]
            qs_name = self.model.objects.filter(name__iexact=arg)
        except:
            qs_name = self.model.objects.none()

        try:
            arg = self.kwargs["surname"]
            qs_surname = self.model.objects.filter(surname__iexact=arg)
        except:
            qs_surname = self.model.objects.none()

        return (qs_name | qs_surname)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Studenti e loro insegnamenti'
        ls = set()
        for s in self.get_queryset():
            for i in models.Insegnamento.objects.all():
                for s in i.studenti.all():
                    ls.add(i)

        context['set_ins'] = ls

        return context