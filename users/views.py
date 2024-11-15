from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserForm


class RegisterView(View):
    def get(self, request):
        create_form = UserForm()
        context = {
            "form": create_form,
        }
        return render(request, "users/register.html", context)

    def post(self, request):

        create_form = UserForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                "form": create_form,
            }
            return render(request, "users/register.html", context)

class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")