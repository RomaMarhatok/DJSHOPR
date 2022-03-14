from typing import Dict, Any
from django.core.validators import MinValueValidator
from django import forms
from products.models import Manufacturer, ProductCategory, Product


class ProductFilterForm(forms.Form):
    STATUS_CHOICES = (
        ("-", ("-")),
        ("phone", ("phone")),
        ("notebook", ("notebook")),
        ("monitor", ("monitor")),
        ("headphones", ("headphones"))
    )
    ORDER_CHOICES = (
        ("-", ("-")),
        ("name", ("name")),
        ("price", ("price")),
        ("-name", ("reverse name")),
        ("-price", ("reverse price"))
    )
    category = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}), required=False)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}), required=False)
    max_price = forms.IntegerField(required=False)
    min_price = forms.IntegerField(required=False)

    def clean_max_price(self):
        data = None if self.cleaned_data['max_price'] is None else self.cleaned_data['max_price']
        return data

    def clean_min_price(self):
        data = None if self.cleaned_data['min_price'] is None else self.cleaned_data['min_price']
        return data

    def clean_category(self):
        query_set_catetory = ProductCategory.objects.filter(
            name=self.cleaned_data['category'])
        if len(query_set_catetory) == 0:
            category_name = None
        else:
            category_name = query_set_catetory[0].pk
        return category_name

    def clean_order_by(self):
        order_by = self.cleaned_data['order_by']
        for name, order in self.ORDER_CHOICES:
            if order_by == name and order_by != "-":
                return name
        return None


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [f.name for f in Product._meta.get_fields() if f.name!="slug"][1:]

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [f.name for f in Product._meta.get_fields() if f.name!="slug"][1:]