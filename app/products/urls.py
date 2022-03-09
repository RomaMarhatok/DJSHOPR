from django.urls import path
from  products.views import IndexListView,ProductDetailView,PorductCreateView, ProductUpdateView
urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('create/',PorductCreateView.as_view(),name="create_product"),
    path('update/<slug:product_slug>/',ProductUpdateView.as_view(),name="create_product"),
    path('<slug:product_slug>/',ProductDetailView.as_view(),name="product_view"),
]