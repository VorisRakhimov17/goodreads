

from django.urls import path
from users.views import RegisterView, LoginView, ProfileView

app_name = 'users'
urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
