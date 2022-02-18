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

