from django.db import models

# Create your models here.

# store category sush as the nootebooks,phones,monitors and etc
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

# store all products attributes wich can be exsist
class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    attributte_name = models.CharField(max_length=255)
    attributte_value = models.CharField(max_length=255) 

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # category_id = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    price = models.FloatField()
    release_date = models.DateField()
    # manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    summary = models.TextField()

    # discount = models.FloatField()

class ProductAttr(models.Model):
    pass
    # attribute_id = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    # product_id = models.ForeignKey(Product,on_delete=models.CASCADE)