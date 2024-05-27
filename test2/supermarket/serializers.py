from django.db.models import ImageField

from rest_framework import serializers, validators

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
        return [obj.__getattribute__(image).url for image in image_fields]


class ShoppingGoodsSerializer(serializers.ModelSerializer):
    buyer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShoppingCart
        fields = 'goods', 'amount', 'buyer', 'id'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ShoppingCart.objects.all(),
                fields=['buyer', 'goods'],
                message='товар уже в корзине'
            )
        ]


class ShoppingCartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    goods = serializers.StringRelatedField()

    class Meta:
        model = ShoppingCart
        fields = ['goods', 'amount', 'total_price']

    def get_total_price(self, obj):
        return obj.amount * obj.goods.price
