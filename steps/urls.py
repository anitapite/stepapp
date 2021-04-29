from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add'),
    path('history', views.history, name = 'history'),
    path('hunindex', views.hunindex, name = 'hunindex'),
]