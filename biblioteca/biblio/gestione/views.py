from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from . import models
from django.utils import timezone
from django.shortcuts import get_object_or_404

MATTONE = 300

def home_page(request):
    return HttpResponse('Benvenuto nella pagina dei soci!')


class LibriList(ListView):
    model = models.libro
    template_name = 'gestione/libro_list.html'
    extra_context = {'title': 'Lista dei Libri'} #passi un title



def lista_libri(request):
    t = "gestione/listalibri.html"

    ctx = {
        "title" : "Lista di libri",
        "listalibri" : models.libro.objects.all()
    }
    return render(request, template_name=t, context=ctx)
    

def mattoni(request):
    t = "gestione/listalibri.html"

    lista_filtrata= models.libro.objects.filter(pagine__gte = MATTONE)

    ctx = {
        "title" : "Lista di mattoni",
        "listalibri" : lista_filtrata
    }
    return render(request, template_name=t, context=ctx)


def crea_libro(request):
    message = ""

    if "autore" in request.GET and "titolo" in request.GET:
        aut = request.GET["autore"]
        tit = request.GET["titolo"]
        pag = 100

        try:
            pag = int(request.GET["pagine"])
        except:
            message = " Pagine non valide. Inserite pagine di default."

        l = models.libro()
        l.autore = aut
        l.titolo = tit
        l.pagine = pag
        l.data_prestito = timezone.now()

        try:
            l.save()
            message = "Creazione libro riuscita!" + message
        except Exception as e:
            message = "Errore nella creazione del libro " + str(e)

    return render(request, template_name="gestione/crealibro.html",
                  context={"title": "Crea Autore", "message": message})



def modifica_libro(request, titolo, autore):
    # Recupera il libro specificato dall'URL
    l = get_object_or_404(models.libro, autore=autore, titolo=titolo)
    message = ""
    
    if request.method == "POST":
        # Se il form viene inviato, aggiorna i dati del libro con quelli inviati
        l.autore = request.POST.get('autore')
        l.titolo = request.POST.get('titolo')
        l.pagine = request.POST.get('pagine')
        
        try:
            l.save()  # Salva le modifiche nel database
            message = "Modifica libro riuscita!"
        except Exception as e:
            message = "Errore nella modifica del libro: " + str(e)
    
    # Se la richiesta è GET, mostra il form con i dati precompilati
    return render(request, "gestione/modificalibro.html", {
        "title": "Modifica libro",
        "message": message,
        "libro": l  # Passa i dati del libro al template
    })


def elimina_libro(request):
    message=""

    l = models.libro.objects.all()

    selected_libro = None

    if request.method == "POST":
        lid = request.POST.get("libro")
        print(lid)
        if lid:
            selected_libro = models.libro.objects.get(pk=lid)
            selected_libro.delete()
            message = "Libro eliminato"
        else:
            message = "Nessun libro eliminato"

    return render(request, template_name="gestione/eliminalibro.html", 
                  context={"title":"Elimina libro", "libri": l, "selected_libro": selected_libro, "message":message})


