from django.urls import include, path
from . import views

app_name = 'soci'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('persona/<int:pk>', views.PersoneDetail.as_view(), name='soci_detail'),
    path('persona-list/', views.PersonaList.as_view(), name='soci_list'),
]
