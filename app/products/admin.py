from django.contrib import admin
from products.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product,ProductAdmin)
class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Manufacturer,ManufacturerAdmin)
class AttributeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Attribute,AttributeAdmin)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProductCategory,ProductCategoryAdmin)




admin.site.register(ProductAttribute)