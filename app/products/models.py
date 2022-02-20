from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(verbose_name = "full manufacturer name",max_length = 255,unique = True)
    slug = models.SlugField(verbose_name = f"slug for manufacturer:{name}",max_length=50, unique = True)
    class Meta:
        verbose_name = ("manufacturer")
        verbose_name_plural = ("manufacturers")
        db_table = 'manufacturer'
    def __str__(self):
        return f"manufacturer:{self.name}"

class Attribute(models.Model):
    name = models.CharField(verbose_name = "full attribute name",max_length=255)
    value = models.CharField(verbose_name = "value of attribute",max_length=255)
    slug = models.SlugField(verbose_name = f"slug for attribute:{name}",max_length=50, unique = True)
    class Meta:
        verbose_name = ("attribute")
        verbose_name_plural = ("attributes")
        db_table = ('attribute')
    def __str__(self):
        return f"attribute:{self.name}"

class ProductCategory(models.Model):
    name = models.CharField(verbose_name = "full category name", max_length=255)
    slug = models.SlugField(verbose_name = "slug for product",max_length=50, unique = True)
    class Meta:
        verbose_name = ('product category name')
        verbose_name_plural = ('product category names')
        db_table = ('product_catogory')
    def __str__(self):
        return f"Product category:{self.name}"

class CategoryAttribute(models.Model):
    category_id = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('category attribute')
        verbose_name_plural = ('category attributes')
        db_table = ('catgory_attribute')

class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,null = True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null = True)
    name = models.CharField(verbose_name = "full product name",max_length=255,unique = True)
    release_date = models.DateField(verbose_name = "product release date")
    price = models.DecimalField(max_digits=15,decimal_places=2,verbose_name = "product price")
    summary = models.TextField(verbose_name = "summary of the product")
    discount = models.DecimalField(max_digits=3,decimal_places=1,verbose_name = "product discount")
    amount = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=3,decimal_places=1,verbose_name = "product rate")
    slug = models.SlugField(verbose_name = "slug for product",max_length = 50, unique = True)
    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('prodcuts')
        db_table = ('product')
    def __str__(self) -> str:
        return f'product {self.name}'