from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from typing import Dict, Any
from products.models import Product
from django.db.models import Q
from products.forms import ProductFilterForm,ProductCreateForm, ProductUpdateForm

class FilterIndexView():
    def filter_product(self, attr_dict, model):
        filtered_dict = {key: value for key,
                         value in attr_dict.items() if not value is None}
        product_query_set = None
        if self.is_tuple_in_dict(('category', 'max_price', 'min_price'), filtered_dict):
            product_query_set = model.objects.filter(Q(category=filtered_dict['category']) & Q(
                price__lte=filtered_dict['max_price'], price__gte=filtered_dict['min_price']))
        elif self.is_tuple_in_dict(('max_price', 'min_price'), filtered_dict):
            product_query_set = model.objects.filter(
                price__lte=filtered_dict['max_price'], price__gte=filtered_dict['min_price'])
        elif 'max_price' in filtered_dict:
            product_query_set = model.objects.filter(price__lte=filtered_dict['max_price'])
        elif 'min_price' in filtered_dict:
            product_query_set = model.objects.filter(price__gte=filtered_dict['min_price'])
        elif 'category' in filtered_dict:
            product_query_set = model.objects.filter(
                category=filtered_dict['category'])
        else:
            product_query_set = model.objects.all()
        if 'order_by' in filtered_dict:
            product_query_set = product_query_set.order_by(
                filtered_dict['order_by'])
        return product_query_set

    def is_tuple_in_dict(self, key_tuple, attr_dict):
        result = all(k in attr_dict for k in key_tuple)
        return result


class IndexListView(ListView, FilterIndexView):
    paginate_by = 5
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"
    form_class = ProductFilterForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context
    def get_queryset(self):
        attr_dict = dict(list(self.request.GET.items())[1:])
        form = self.form_class(attr_dict)
        if form.is_valid():
            products = self.filter_product(form.cleaned_data, self.model)
            return products
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    template_name = "products/view.html"


class PorductCreateView(CreateView):
    form_class = ProductCreateForm
    template_name = "products/create.html"
    def get(self,request,*args,**kwargs):
        context = {'form': self.form_class(),'value': 'create'}
        return render(request=request,template_name=self.template_name,context=context)



class ProductUpdateView(UpdateView):
    model=Product
    form_class = ProductUpdateForm
    template_name = "products/update.html"
    slug_url_kwarg = 'product_slug'
    def get(self,request,*args,**kwargs):
        context = {'form': self.form_class(),'value': 'update'}
        return render(request=request,template_name=self.template_name,context=context)