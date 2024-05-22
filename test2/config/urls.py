from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from supermarket.views import CategoryViewSet

supermarket_router = DefaultRouter()
supermarket_router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),
    re_path(r'', include(supermarket_router.urls)),
]
