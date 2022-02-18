from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(verbose_name = "full manufacturer name",max_length = 255,unique = True)
    slug = models.CharField(verbose_name = f"slug for manufacturer:{name}",max_length=255, unique = True)
    class Meta:
        verbose_name = ("manufacturer")
        verbose_name_plural = ("manufacturers")
    def __str__():
        return f"manufacturer:{name}"

class Attribute(models.Model):
    name = models.CharField(verbose_name = "full attribute name",max_length=255)
    value = models.CharField(verbose_name = "value of attribute",max_length=255)
    slug = models.CharField(verbose_name = f"slug for attribute:{name}",max_length=255, unique = True)
    class Meta:
        verbose_name = ("attribute")
        verbose_name_plural = ("attributes")
    def __str__():
        return f"attribute:{name}"

class ProductCategory(models.Model):
    name = models.CharField(verbose_name = "full category name", max_length=255)
    slug = models.CharField(verbose_name = "slug for product",max_length=255, unique = True)
    class Meta:
        verbose_name = ('product category name')
        verbose_name_plural = ('product category names')
    def __str__():
        return f"Product category:{name}"

class CategoryAttribute(models.Model):
    category_id = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('category attribute')
        verbose_name_plural = ('category attributes')

class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,null = True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null = True)
    title = models.CharField(verbose_name= "full product name",max_length=255,unique = True)
    release_date = models.DateField(verbose_name= "product release date")
    price = models.DecimalField(max_digits=15,decimal_places=2,verbose_name = "product price")
    summary = models.TextField(verbose_name = "summary of the product")
    discount = models.DecimalField(max_digits=3,decimal_places=1,verbose_name = "product discount")
    amount = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=3,decimal_places=1,verbose_name = "product rate")
    slug = models.CharField(verbose_name = "slug for product",max_length = 255, unique = True)
    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('prodcuts')