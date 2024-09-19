import sys
import os

# Aggiungi la root del progetto Django al percorso Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imposta il modulo di impostazioni di Django (se non già impostato)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblio2.settings')

# Importa le impostazioni di Django e avvia il setup
import django
django.setup()

from gestione.models import Libro
from django.utils import timezone
from datetime import datetime


def erase_db():
    print("Cancello il DB")
    Libro.objects.all().delete()


def init_db():
    if len(Libro.objects.all()) != 0:
        return

    def func_time(off_year=None, off_month=None, off_day=None):
        tz = timezone.now()
        out = datetime(tz.year - off_year, tz.month - off_month, tz.day - off_day, tz.hour, tz.minute, tz.second)
        return out

    libridict = {
        "autori": ["Alessandro Manzoni", "George Orwell", "Omero", "George Orwell", "Omero"],
        "titoli": ["Promessi Sposi", "1984", "Odissea", "La fattoria degli animali", "Iliade"],
        "pagine": [824, 328, 414, 131, 264],
        "date": [func_time(y, m, d) for y in range(2) for m in range(2) for d in range(2)]
    }

    for i in range(5):
        l = Libro()
        for k in libridict:
            if k == "autori":
                l.autore = libridict[k][i]
            if k == "titoli":
                l.titolo = libridict[k][i]
            if k == "pagine":
                l.pagine = libridict[k][i]
            else:
                l.data_prestito = libridict[k][i]
        # print(l)
        l.save()

    print("Dumb db")
    print(Libro.objects.all())