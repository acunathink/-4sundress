from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from supermarket.views import (CategoryViewSet, GoodsViewSet,
                               ShoppingCartAPIView, ShoppingGoodsViewSet)

supermarket_router = DefaultRouter()
supermarket_router.register(r'categories', CategoryViewSet)
supermarket_router.register(r'goods', GoodsViewSet)
supermarket_router.register(r'shopping_goods', ShoppingGoodsViewSet,
                            basename='shopping_goods')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),
    path('shopping_cart/', ShoppingCartAPIView.as_view()),
    re_path(r'', include(supermarket_router.urls)),
]
