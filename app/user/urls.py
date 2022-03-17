from django.urls import path
from user.views import RegistrationView

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration")
    ]
