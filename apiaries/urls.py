from django.contrib import admin
from django.urls import path, include
from apiaries.views import CreateApiaryAPIView, \
   ListApiaryAPIView, UpdateApiaryAPIView, DeleteApiaryAPIView

urlpatterns = [
   path('create/', CreateApiaryAPIView.as_view(), name='apiary-create'),
   path('list/', ListApiaryAPIView.as_view(), name='apiary-list'),
   path('update/<int:pk>', UpdateApiaryAPIView.as_view(), name='apiary-update'),
   path('delete/<int:pk>', DeleteApiaryAPIView.as_view(), name='apiary-delete'),
]