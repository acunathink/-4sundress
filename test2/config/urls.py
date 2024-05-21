from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),
]
