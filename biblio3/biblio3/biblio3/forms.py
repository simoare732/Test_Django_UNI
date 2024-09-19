from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

class CreaUtenteLettore(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name='Lettori')
        g.user_set.add(user)
        return user


class CreaUtenteBibliotecario(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name='Bibliotecari')
        g.user_set.add(user)
        return user