from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home(request):
    login_ok = request.GET.get('login') == 'ok'
    return render(request, 'h.html', {'login_ok': login_ok})

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('login')

