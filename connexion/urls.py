from django.urls import path

from connexion import views

urlpatterns = [
    path('creer/', views.creer, name='creer'),
    path('connecter/', views.connecter , name='connecter'),
    path('mon/', views.mon, name='mon'),
]
