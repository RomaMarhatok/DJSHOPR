from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product,ProductCategory,Manufacturer,ProductAttribute
# Create your views here.

def index(request):
    products = Product.objects.values()
    for i in products:
        i['manufacturer'] = Manufacturer.objects.get(pk = i['manufacturer_id_id'])
    attributes = products[0].keys()
    return render(request,'index.html',context={'attributes':attributes,'products':products})

def view(request,slug):
    print(slug)
    return HttpResponse('hello')