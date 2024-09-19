from iscrizioni.models import Studente, Insegnamento

def erase_db():
    print("Cancello il DB")
    Studente.objects.all().delete()
    Insegnamento.objects.all().delete()

def init_db():
    if Studente.objects.all().count() > 0:
        return

    lista_studenti = [
        ("Mario", "Bianchi"),
        ("Luigi", "Verdi"),
        ("Giovanni", "Rossi"),
        ("Maria", "Viola"),
        ("Antonia", "Azzurri")
    ]

    lista_insegnamenti = [
        "Programmazione ad oggetti",
        "Programmazione 1",
        "Tecnologie web",
        "Algoritmi e strutture dati",
        "Algebra lineare"
    ]

    for s in lista_studenti:
        s_db = Studente()
        s_db.name = s[0]
        s_db.surname = s[1]
        s_db.save()

    studenti = Studente.objects.all()

    for index, ins in enumerate(lista_insegnamenti):
        ins_db = Insegnamento()
        ins_db.titolo = ins
        ins_db.save()

        if index == 0: continue
        count = 0
        for s in studenti:
            ins_db.studenti.add(s)
            count += 1
            if count > index:
                break

    print("DUMB DB")
    print("Studenti")
    for s in studenti:
        print(s)

    print("Insegnamenti")
    for i in Insegnamento.objects.all():
        print(i)
        print("Studenti iscritti " + str(i.studenti.all()))