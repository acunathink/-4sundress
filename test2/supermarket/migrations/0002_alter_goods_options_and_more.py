# Generated by Django 5.0.6 on 2024-05-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('buyer', 'goods'), name='unique_goods_in_cart'),
        ),
    ]