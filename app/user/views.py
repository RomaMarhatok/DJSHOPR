from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from user.forms import RegistrationForm, SingInForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from user.models import BasketProduct, Basket
from products.models import Product
from django.contrib.auth import logout, login


class RegistrationView(View):
    template_name = "user/registration/registration.html"
    form_class = RegistrationForm
    model = User

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username", None)
            password = form.cleaned_data.get("password", None)
            email = form.cleaned_data.get("email", None)
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            Basket.objects.create(user__id=User.objects.filter(username=user)[0].pk)
            return reverse_lazy("sign_in")
        else:
            return render(request, self.template_name, context={"form": form})


class SingInView(LoginView):
    template_name = "user/registration/sign_in.html"
    form_class = SingInForm
    model = User

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["form"] = self.form_class
        return context_data

    def get_success_url(self) -> str:
        return reverse_lazy("index")


class BasketListView(ListView):
    template_name = "user/basket.html"
    model = BasketProduct
    context_object_name = "products"

    def get_queryset(self):
        user_pk = User.objects.filter(username=self.request.user)[0].pk
        basket = Basket.objects.filter(user__id=user_pk)
        basketproducts_queryset = BasketProduct.objects.filter(basket__id=basket[0].pk)
        products_name = [
            basketproduct.product for basketproduct in basketproducts_queryset
        ]
        products_name
        product_queryset = Product.objects.filter(name__in=products_name)
        return product_queryset


def logout_user(request):
    logout(request)
    return redirect("sign_in")
