from django.contrib import admin

from .models import Category, CustomUser, Goods, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 'image'
    search_fields = 'name', 'slug'
    list_editable = 'slug',
    list_display_links = 'name',


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 'image', 'category'
    search_fields = 'name', 'slug'
    list_editable = 'slug',
    list_display_links = 'name',
    list_filter = 'category',


class CustomUserAdmin(admin.ModelAdmin):
    list_display = 'username', 'email', 'is_staff'
    list_editable = 'is_staff',
    search_fields = 'email', 'username'
    list_display_links = 'username',


class GoodsAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 'price', 'subcategory'
    list_display_links = 'name',
    list_editable = 'price',
    search_fields = 'price', 'slug', 'name'
    list_filter = 'category', 'subcategory'


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Goods, GoodsAdmin)
