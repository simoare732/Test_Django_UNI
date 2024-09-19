from django.urls import path, include
from . import views
from .views import RestituisciView

app_name = 'gestione'
urlpatterns = [

    path('', views.gestione_home, name='home'),
    path('libri/', views.LibroListView.as_view(), name='lista_libri'),
    path('search/', views.search, name='ricerca'),
    path('search/<str:sstring>/<str:where>/', views.LibroRicercaView.as_view(), name='ricerca_risultati'),
    path('prestito/<int:pk>/', views.prestito, name='prestito'),
    path('situation/', views.my_situation, name='situation'),
    path('ricerca/gethint/', views.get_hint, name='get_hint'),

    path('restituzione/<pk>', RestituisciView.as_view(), name='restituzione'),

]