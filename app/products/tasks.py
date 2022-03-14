
from celery import shared_task
from products.models import Product
from django.db.models import Q
@shared_task(name="products.tasks.get_all_products")
def get_all_porducts(attr_dict):
    filtered_dict = {key: value for key,
                         value in attr_dict.items() if not value is None}
    product_query_set = None

    if  is_tuple_in_dict(('category', 'max_price', 'min_price'), filtered_dict):
        product_query_set = Product.objects.filter(Q(category=filtered_dict['category']) & 
        Q(price__lte=filtered_dict['max_price'], price__gte=filtered_dict['min_price']))

    elif is_tuple_in_dict(('max_price', 'min_price'), filtered_dict):
        product_query_set = Product.objects.filter(
            price__lte=filtered_dict['max_price'], price__gte=filtered_dict['min_price'])
    
    elif 'min_price' in filtered_dict:
        product_query_set = Product.objects.filter(price__gte=filtered_dict['min_price'])

    elif 'category' in filtered_dict:
        product_query_set = Product.objects.filter(category=filtered_dict['category'])

    elif 'max_price' in filtered_dict:
        product_query_set = Product.objects.filter(price__lte=filtered_dict['max_price'])
    else:
        product_query_set = Product.objects.all()
    if 'order_by' in filtered_dict:
        product_query_set = product_query_set.order_by(
            filtered_dict['order_by'])
            
    product_list = [prodcut.to_dict() for prodcut in product_query_set]
    return product_list

def is_tuple_in_dict(key_tuple, attr_dict):
    result = all(k in attr_dict for k in key_tuple)
    return result
