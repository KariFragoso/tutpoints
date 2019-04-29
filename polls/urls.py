
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:question_id>/first/', views.first, name='first'),

    path('newquestion/', views.newquestion, name='newquestion'),

    path('newchoice/', views.newchoice, name='newchoice'),

    path('list/', views.list, name='list'),
    path('<int:pk>/edit/', views.editquestion, name='editquestion'),
    path('<int:pk>/delete/', views.deletequestion, name='deletequestion'),
    
    path('choices/list/', views.listchoices, name='listchoices'),
    path('choices/<int:pk>/edit/', views.editchoice, name='editchoice'),
    path('choices/<int:pk>/delete/', views.deletechoice, name='deletechoice'),
    
]