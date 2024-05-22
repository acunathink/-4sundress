from rest_framework import pagination, permissions, viewsets

from .models import Category, Goods, ShoppingCart
from .serializers import CategorySerializer, GoodsSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    pagination_class = pagination.LimitOffsetPagination


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoodsSerializer
    pagination_class = pagination.LimitOffsetPagination


class ShoppingCartViewSet(viewsets.ModelViewSet):
    pass
