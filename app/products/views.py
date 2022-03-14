from products import tasks
from audioop import reverse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from typing import Dict, Any
from products.models import Product
from django.db.models import Q
from products.forms import ProductFilterForm,ProductCreateForm, ProductUpdateForm
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

    def get_queryset(self):
        attr_dict = dict(list(self.request.GET.items())[1:])
        form = self.form_class(attr_dict)
        if form.is_valid():
            products = tasks.get_all_porducts.delay(form.cleaned_data).get()
            return products
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    template_name = "products/view.html"


class PorductCreateView(CreateView):
    form_class = ProductCreateForm
    template_name = "products/create.html"
    extra_context = {'value':'create'}

    def get_object(self):
        slug_ = self.kwargs.get('product_slug')
        return get_object_or_404(Product,slug = slug_)


class ProductUpdateView(UpdateView):
    model=Product
    form_class = ProductUpdateForm
    template_name = "products/update.html"
    slug_url_kwarg = 'product_slug'
    extra_context = {'value':'update'}

    def get_object(self):
        slug_ = self.kwargs.get('product_slug')
        return get_object_or_404(Product,slug = slug_)

    def get_success_url(self) -> str:
        return reverse('index')

class ProductDeleteView(DeleteView):
    template_name = "products/delete.html"
    context_object_name = "product"
    slug_url_kwarg = 'product_slug'
    extra_context = {'value':'delete'}

    def get_object(self):
        slug_ = self.kwargs.get('product_slug')
        return get_object_or_404(Product,slug = slug_)

    def get_success_url(self) -> str:
        return reverse('index')