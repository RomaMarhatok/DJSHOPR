from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(verbose_name = "full manufacturer name",max_length = 255,unique = True)
    slug = models.SlugField(verbose_name = "slug for manufacturer",max_length=50, unique = True)
    class Meta:
        verbose_name = ("manufacturer")
        verbose_name_plural = ("manufacturers")
        db_table = 'manufacturer'
    def __str__(self)->str:
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Manufacturer).save(*args,**kwargs)


class Attribute(models.Model):
    name = models.CharField(verbose_name = "full attribute name",max_length=255)
    slug = models.SlugField(verbose_name = "slug for attribute",max_length=50, unique = True)
    class Meta:
        verbose_name = ("attribute")
        verbose_name_plural = ("attributes")
        db_table = ('attribute')
    def __str__(self)->str:
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Attribute).save(*args,**kwargs)

class ProductCategory(models.Model):
    name = models.CharField(verbose_name = "full category name", max_length=255)
    slug = models.SlugField(verbose_name = "slug for category",max_length=50, unique = True)
    class Meta:
        verbose_name = ('product category name')
        verbose_name_plural = ('product category names')
        db_table = ('product_category')
    def get_absolute_url(self):
        return reverse('category_view',kwargs={'category_slug':self.slug})
    def __str__(self)->str:
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory).save(*args,**kwargs)
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,null = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null = True)
    name = models.CharField(verbose_name = "full product name",max_length=255,unique = True)
    release_date = models.DateField(verbose_name = "product release date",null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,verbose_name = "product price")
    summary = models.TextField(verbose_name = "summary of the product",blank=True)
    discount = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    amount = models.PositiveIntegerField(verbose_name="product amount")
    rate = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],verbose_name = "product rate")
    slug = models.SlugField(verbose_name = "slug for product",max_length = 50, unique = True)
    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('prodcuts')
        db_table = ('product')

    def get_absolute_url(self):
        return reverse('product_view',kwargs={'product_slug':self.slug})
    def __str__(self) -> str:
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product).save(*args,**kwargs)
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    attribute_value = models.CharField(verbose_name="atribute value",max_length=255)
    class Meta:
        verbose_name = ('product attribute')
        verbose_name_plural = ('product attributes')
        db_table = ('product_attribute')
    def __str__(self) -> str:
        return f'atrribute:{self.attribute} | product {self.product}'