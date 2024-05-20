from django.db import models

class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=64,
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        verbose_name='slug-имя'
        max_length=64,
        unique=True,
        null=False,
        blank=False
    )
    image = models.ImageField(
        upload_to='images/',
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return self.name

class SubCategory(Category):
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE
    )
