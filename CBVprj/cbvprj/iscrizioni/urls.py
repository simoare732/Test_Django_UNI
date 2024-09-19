from django.template.context_processors import request
from django.urls import path
from . import views

app_name = 'iscrizioni'

urlpatterns = [
    path('', views.index, name='index'),
    path('listastudenti/', views.ListaStudentiView.as_view(), name='listastudenti'),
    path('insegnamentiattivi/', views.ListaInsegnamentiAttivi.as_view(), name='insegnamentiattivi'),
    path('listainsegnamenti', views.ListaInsegnamentiView.as_view(), name='listainsegnamenti'),
    path('studenticonta', views.ListaStudentiIscritti.as_view(), name='studenticonta'),
    path('creastudente/', views.CreateStudenteView.as_view(), name='creastudente'),
    path('creainsegnamento/', views.CreateInsegnamentoView.as_view(), name='creainsegnamento'),
    path('insegnamento/<pk>/', views.DetailInsegnamentoView.as_view(), name='insegnamento' ),
    path('editinsegnamento/<int:pk>', views.UpdateInsegnamentoView.as_view(), name='editinsegnamento'),
    path('cancellastudente/<pk>', views.DeleteStudenteView.as_view(), name='cancellastudente'),
    path('cancellainsegnamento/<pk>', views.DeleteInsegnamentoView.as_view(), name='cancellainsegnamento'),
    path('cercastudente/', views.cerca_studenti, name='cercastudente'),
]