from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('apiaries/', include('apiaries.urls')),
    path('hives/', include('hives.urls')),
    path('frames/', include('frames.urls'))
]
