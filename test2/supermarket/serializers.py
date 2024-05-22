from rest_framework import serializers

from .models import Category, ShoppingCart, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = 'id', 'name', 'slug'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'slug', 'subcategories'
