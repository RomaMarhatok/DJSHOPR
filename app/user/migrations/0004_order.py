# Generated by Django 3.2 on 2022-03-15 16:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_basketproduct'),
    ]

    operations = [
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
