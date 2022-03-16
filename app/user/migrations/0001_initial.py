# Generated by Django 4.0.3 on 2022-03-16 13:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0018_alter_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
                'db_table': 'basket',
            },
        ),
        migrations.CreateModel(
            name='BasketProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
            options={
                'verbose_name': 'product in basket',
                'verbose_name_plural': 'products in baskets',
                'db_table': 'produc_basket',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='order price')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='amount of product in order')),
                ('basket_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.basketproduct')),
            ],
        ),
    ]
