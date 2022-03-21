from django.urls import path
from user.views import RegistrationView, SingInView, logout_user, BasketListView,BasketView,delete_product_from_basket

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("sign in/", SingInView.as_view(), name="sign_in"),
    path("logout/", logout_user, name="logout"),
    path("basket/", BasketListView.as_view(), name="basket"),
    path("add/",BasketView.as_view(),name="add_product"),
    path("delete/<slug:product_slug>/",delete_product_from_basket,name="delete_product_from_basket")
]
