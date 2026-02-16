from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),
]
