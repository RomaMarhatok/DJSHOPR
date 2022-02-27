from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.shortcuts import render,redirect
from django.urls import reverse
from typing import Dict,Any
from products.models import Product,ProductCategory
from django.db.models import Q
from products.forms import ProductFilterForm
# Create your views here.


class IndexListView(ListView):
    paginate_by = 2
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"
    form_class = ProductFilterForm
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context
    def post(self,request,*args,**kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']
            min_price = form.cleaned_data['min_price']
            order_by = form.cleaned_data['order_by']
            products = self.model.objects.all()
            print(products)
            
            if category_name is None and not (max_price<0 and min_price>=max_price):
                products = self.model.objects.filter(price__lte = max_price,price__gte = min_price)
            elif not category_name is None:
                products = self.model.objects.filter(category = category_name)
            elif not category_name is None and not (max_price<0 and min_price>=max_price):
                products = self.model.objects.filter(Q(category = category_name) & Q(price__lte = max_price,price__gte = min_price))
            
            if not order_by is None:
                products = products.order_by(order_by)
            return render(request,'products/index.html',context={'products':products,'form':self.form_class})
            
            #guery_set_category = ProductCategory.objects.filter(name = category_name)
            # if len(guery_set_category)!=0:
            #     product_category = ProductCategory.objects.filter(name=category_name).get()
            #     products = self.model.objects.filter(Q(category = product_category) | Q(price__lte = max_price,price__gte = min_price))
                #return render(request,'products/index.html',context={'products':products,'form':self.form_class})
            # else:
            #     products = Product.objects.all()
            #     url = reverse('index')
            #     print(url)
                #return redirect(url,context={'products':products,'form':self.form_class})
                # return redirect(request,'products/index.html',context={'products':products,'form':self.form_class})



class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    template_name = "products/view.html"


class PorductCreateView(CreateView):
    model = Product
    fields = [f.name for f in Product._meta.get_fields()][1:]
    template_name = "products/create.html"
    extra_content = {'value':'create'}

class ProductUpdateView(UpdateView):
    model = Product
    fields = [f.name for f in Product._meta.get_fields()][1:]
    template_name = "products/create.html"
    extra_content = {'value':'update'}