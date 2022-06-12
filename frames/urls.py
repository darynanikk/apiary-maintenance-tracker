from django.urls import path, include

from frames.views import CreateFrameAPIView, ListFrameAPIView, ListUserFramesByHiveAPIView, UpdateFrameAPIView, \
    DeleteFrameAPIView


urlpatterns = [
   path('create/', CreateFrameAPIView.as_view(), name='frame-create'),
   path('list/', ListFrameAPIView.as_view(), name='frame-list'),
   path('list/<int:hive_id>', ListUserFramesByHiveAPIView.as_view(), name='frames-by-apiary'),
   path('update/<int:pk>', UpdateFrameAPIView.as_view(), name='frame-update'),
   path('delete/<int:pk>', DeleteFrameAPIView.as_view(), name='frame-delete'),
]