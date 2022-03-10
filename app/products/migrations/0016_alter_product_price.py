# Generated by Django 4.0.2 on 2022-03-08 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='product price'),
        ),
    ]
