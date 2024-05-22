from django.db.models import ImageField
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy

from rest_framework import exceptions, serializers, validators

from .models import Category, Goods, ShoppingCart, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = 'id', 'name', 'slug'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'slug', 'subcategories'


class GoodsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    image_list = serializers.SerializerMethodField()

    class Meta:
        model = Goods
        fields = (
            'name', 'slug', 'category', 'subcategory', 'price', 'image_list'
        )

    def get_image_list(self, obj: Goods):
        image_fields = [field.name for field in Goods._meta.get_fields()
                        if isinstance(field, ImageField)]
        image_list = [
            obj.__getattribute__(image).url for image in image_fields
        ]
        return image_list


class GoodsSerializerField(serializers.Field):
    def run_validation(self, data):
        if not isinstance(data, int):
            raise exceptions.ValidationError(gettext_lazy(
                f"expected a number but got '{data}'"))
        return super().run_validation(data)

    def to_internal_value(self, data):
        obj = get_object_or_404(Goods, pk=data)
        return obj

    def to_representation(self, obj):
        return obj.name


class ShoppingCartSerializer(serializers.ModelSerializer):
    goods = GoodsSerializerField()
    buyer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShoppingCart
        fields = 'goods', 'amount', 'buyer',  # 'id'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ShoppingCart.objects.all(),
                fields=['buyer', 'goods'],
                message='товар уже в корзине'
            )
        ]
