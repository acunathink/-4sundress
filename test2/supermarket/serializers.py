from django.db.models import ImageField

from rest_framework import serializers

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
    category = serializers.CharField()
    subcategory = serializers.CharField()
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
