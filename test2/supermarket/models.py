from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class BaseCategory(models.Model):
    name = models.CharField(verbose_name='Наименование',
                            max_length=64, unique=True,
                            null=False, blank=False)
    slug = models.SlugField(verbose_name='slug-имя',
                            max_length=64, unique=True,
                            null=False, blank=False)
    image = models.ImageField(upload_to='images/category/',
                              null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class Category(BaseCategory):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(BaseCategory):
    category = models.ForeignKey(Category, related_name='subcategories',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Goods(models.Model):
    name = models.CharField(verbose_name='Наименование',
                            max_length=64, unique=True,
                            null=False, blank=False)
    category = models.ForeignKey(Category, related_name='goods',
                                 on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='items',
                                    on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='slug-имя',
                            max_length=64, unique=True,
                            null=False, blank=False)
    large_image = models.ImageField(upload_to='images/goods/large',
                                    null=False, blank=False)
    medium_image = models.ImageField(upload_to='images/goods/medium',
                                     null=False, blank=False)
    small_image = models.ImageField(upload_to='images/goods/small',
                                    null=False, blank=False)
    price = models.IntegerField(verbose_name='Цена', null=False,
                                validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class ShoppingCart(models.Model):
    buyer = models.ForeignKey(CustomUser, related_name='cart',
                              on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='in_cart',
                              on_delete=models.CASCADE)
    amount = models.SmallIntegerField(verbose_name='Количество', null=False,
                                      validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['buyer', 'goods'],
                name='unique_goods_in_cart'
            )
        ]
