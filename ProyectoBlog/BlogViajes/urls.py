from django.contrib import admin
from django.urls import path
from BlogViajes import views

urlpatterns = [
    path('', views.principal, name="principal"),
    path('agregar/', views.agregar, name="agregar"),
    path('buscar/', views.buscar, name="buscar"),
]