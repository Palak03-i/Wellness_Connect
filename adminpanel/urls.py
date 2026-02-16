from django.urls import path
from .views import admin_dashboard

urlpatterns = [
    path('', admin_dashboard, name='admin_home'),   # 👈 ADD THIS
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
]
