from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
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
        login_form = AuthenticationForm()


        return render(request, "users/login.html", {"login_form": login_form})

    def post(self, request):

        login_form = AuthenticationForm(data= request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user) # Bu tayyor funksiya login uchun ishlatiladi

            return redirect("landing_page")
        else:
            return render(request, "users/login.html", {"login_form": login_form})