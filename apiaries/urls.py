from django.contrib import admin
from django.urls import path, include
from apiaries.views import CreateApiaryAPIView, ListApiaryAPIView

urlpatterns = [
   path('create/', CreateApiaryAPIView.as_view(), name='create-apiary'),
   path('list/', ListApiaryAPIView.as_view(), name='list-apiary'),
   # path('update/'),
   # path('delete/'),
]