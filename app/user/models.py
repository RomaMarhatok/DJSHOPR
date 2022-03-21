from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "basket"
        verbose_name_plural = "baskets"
        db_table = "basket"


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "product in basket"
        verbose_name_plural = "products in baskets"
        db_table = "produc_basket"


class Order(models.Model):
    basket_product = models.ForeignKey(BasketProduct, on_delete=models.PROTECT)
    price = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=15,
        decimal_places=2,
        verbose_name="order price",
    )
    amount = models.PositiveSmallIntegerField(verbose_name="amount of product in order")
