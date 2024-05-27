from rest_framework import permissions, status, views, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Category, Goods, ShoppingCart
from .serializers import (CategorySerializer, GoodsSerializer,
                          ShoppingCartSerializer, ShoppingGoodsSerializer)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoodsSerializer
    pagination_class = LimitOffsetPagination


class ShoppingGoodsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = ShoppingGoodsSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)


class ShoppingCartAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        cart_items = ShoppingCart.objects.filter(buyer=user)
        serializer = ShoppingCartSerializer(cart_items, many=True)

        total_cost = sum(item['total_price'] for item in serializer.data)

        response_data = {
            'items': serializer.data,
            'total_cost': total_cost
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request):
        ShoppingCart.objects.filter(buyer=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
