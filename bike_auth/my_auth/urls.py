from django.contrib.auth.views import LoginView
from django.urls import path

from my_auth.views import RegisterFormView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
