from django.contrib import admin
from user.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Basket)
admin.site.register(BasketProduct)
admin.site.register(Order)

