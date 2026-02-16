from django.urls import path
from .views import counsellor_dashboard

urlpatterns = [
    path('', counsellor_dashboard, name='counsellor_dashboard'),
]
