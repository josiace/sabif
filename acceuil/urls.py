from django.urls import path

from acceuil import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('blogs/', views.contenu , name='blogs'),
]
