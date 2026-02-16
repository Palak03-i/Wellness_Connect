from django.urls import path
from .views import user_login, register_view, home_redirect

urlpatterns = [
    path('', home_redirect, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register_view, name='register'),
]
