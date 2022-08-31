from django.contrib.auth.views import LoginView
from django.urls import path

from my_auth.views import RegisterFormView, user_details

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user_details/<str:session_id>', user_details, name='user_details'),
]
