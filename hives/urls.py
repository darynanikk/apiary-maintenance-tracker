from django.urls import path, include

from hives.views import CreateHiveAPIView, ListHiveAPIView, UpdateHiveAPIView, DeleteHiveAPIView

urlpatterns = [
   path('create/', CreateHiveAPIView.as_view(), name='hive-create'),
   path('list/', ListHiveAPIView.as_view(), name='hive-list'),
   path('update/<int:pk>', UpdateHiveAPIView.as_view(), name='hive-update'),
   path('delete/<int:pk>', DeleteHiveAPIView.as_view(), name='hive-delete'),
]