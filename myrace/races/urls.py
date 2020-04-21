from django.urls import path

from . import views

app_name = 'races'

urlpatterns = [
    # ex: /races/
    path('', views.index, name='index'),

    # ex: /races/2
    path('<int:race_id>/', views.detail, name='detail'),

]


# code avant mise à jour pour utilisation des vues génériqes
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
   
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
   
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
   
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]