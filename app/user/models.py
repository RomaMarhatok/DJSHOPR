from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.hashers import Argon2PasswordHasher, BasePasswordHasher
class User(models.Model):
    login = models.CharField(verbose_name = "user login",max_length = 255,unique=True)
    password = models.CharField(verbose_name = "user password",max_length = 255,unique=True)
    username = models.CharField(verbose_name = "user name",max_length = 255,unique=True)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        db_table = ('user')
    
    def save(self,*args,**kwargs):
        self.password = Argon2PasswordHasher().encode(self.password,BasePasswordHasher().salt())
        super(User,self).save(*args,**kwargs)
class Basket(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('basket')
        verbose_name_plural = ('baskets')
        db_table = ('basket')

class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket,on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product',on_delete=models.PROTECT)

    class Meta:
        verbose_name = ('product in basket')
        verbose_name_plural = ('products in baskets')
        db_table = ('produc_basket')

class Order(models.Model):
    basket_product = models.ForeignKey(BasketProduct,on_delete=models.PROTECT)
    price = models.DecimalField(validators=[MinValueValidator(0.0)],max_digits=15,decimal_places=2,verbose_name = "order price")
    amount = models.PositiveSmallIntegerField(verbose_name="amount of product in order")
