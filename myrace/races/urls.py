from django.urls import path

from . import views

app_name = 'races'

urlpatterns = [
    # ex: /races/
    path('', views.index, name='index'),

    # ex: /race_list/
    path('race_list', views.race_list, name='race_list'),

    # ex: /races/2
    path('<int:race_id>/', views.detail, name='detail'),

    # ex: /races/search/
    path('search', views.search_results, name='search_results'),

]
