from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from user.forms import RegistrationForm
from django.contrib.auth.models import User


class RegistrationView(View):
    template_name = "user/registration/registration.html"
    form_class = RegistrationForm
    model = User

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        d2 = {key: value[0] for key, value in request.POST.items()}
        return HttpResponse(d2)
