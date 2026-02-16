from django.urls import path
from .views import student_dashboard

app_name = 'student'

urlpatterns = [
    path('', student_dashboard, name='student_dashboard'),
]
