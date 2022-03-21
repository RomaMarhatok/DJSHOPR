from django.urls import path
from user.views import RegistrationView, SingInView,logout_user

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("sign in/", SingInView.as_view(), name="sign_in"),
    path("logout/",logout_user,name="logout"),
    
]
