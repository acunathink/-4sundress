from rest_framework import pagination, permissions, viewsets

from .models import Category, Goods, ShoppingCart
from .serializers import (CategorySerializer, GoodsSerializer,
                          ShoppingCartSerializer)


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
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
        # return super().perform_create(serializer)
