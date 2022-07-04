# chat/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.Test.as_view()),
    path('room/<int:pk>/', views.room, name='room'),
    path('', views.index, name='index'),
]