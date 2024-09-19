from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollListView.as_view(), name='index'),
    path('<int:pk>/detail/', views.PollDetailView.as_view(), name='detail'),
    path('search/', views.search, name="search"),
    path('searchresults/<str:sstring>/<str:where>/', views.SearchResultsView.as_view(), name='searchresults'),
    path('vote/<int:pk>/', views.vote, name='vote'),
    path('votecasted/<int:pk>/<str:answer>/', views.VoteCastedDetail.as_view(), name='votecasted'),

    path('createquestion/', views.CreateQuestionView.as_view(), name='createquestion'),
    path('createchoice/', views.CreateChoiceView.as_view(), name='createchoice'),
]

