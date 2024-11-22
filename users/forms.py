from django import forms
from django.contrib.auth.models import User


# class UserForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)
#
#     def save(self):
#         username = self.cleaned_data['username']
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         user = User.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email
#         )
#
#         user.set_password(password)  # set_password ning vazifasi hash lab beradi parolni
#         user.save()
#         return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user




