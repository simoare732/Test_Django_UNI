# models.py
from django.db import models

class Ruolo(models.Model):
    titolo = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Ruoli'

class Persona(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    ruolo = models.ForeignKey(Ruolo, on_delete=models.PROTECT, related_name='persone')

    class Meta:
        verbose_name_plural = 'Persone'



