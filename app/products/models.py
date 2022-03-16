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
        super(Manufacturer,self).save(*args,**kwargs)


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
        super(Attribute,self).save(*args,**kwargs)

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
        super(ProductCategory,self).save(*args,**kwargs)
    def to_dict(self):
        data={
            'id':self.pk,
            'name':str(self.name),
            'slug':self.slug
        }
        return data

def content_product_file_path(instance,filename):
    return "/".join(['products',instance.name,'%Y','%m','%d',filename])
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,null = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL,null = True)
    name = models.CharField(verbose_name = "full product name",max_length=255,unique = True)
    release_date = models.DateField(verbose_name = "product release date",null=True)
    price = models.DecimalField(validators=[MinValueValidator(0.0)],max_digits=15,decimal_places=2,verbose_name = "product price")
    summary = models.TextField(verbose_name = "summary of the product",blank=True)
    discount = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],null=True,verbose_name="product discount")
    amount = models.PositiveIntegerField(verbose_name="product amount")
    rate = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],verbose_name = "product rate")
    slug = models.SlugField(verbose_name = "slug for product",max_length = 50, unique = True)
    image = models.ImageField(upload_to = content_product_file_path,null=True,blank = True)
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
        super(Product,self).save(*args,**kwargs)
    
    def __validate_path_image(self):
        photo_url = None
        try:
            photo_url = self.image.url
            return photo_url
        except ValueError:
            photo_url = ""
        return photo_url

    def to_dict(self):
        data = {
            'id':self.pk,
            'category':str(self.category),
            'name':self.name,
            'summary':self.summary,
            'price':str(self.price),
            'absolute_url':self.get_absolute_url(),
            'image_url':self.__validate_path_image()
        }
        return data
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