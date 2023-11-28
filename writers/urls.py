from django.contrib import admin
from django.urls import path, include
from writers import views

urlpatterns = [
    path('', views.writers, name='writers'),
    path('<str:slug>', views.userView, name='userView')
]

