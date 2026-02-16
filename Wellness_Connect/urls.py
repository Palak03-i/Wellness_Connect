from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('counsellor/', include('counsellor.urls')),
    path('adminpanel/', include('adminpanel.urls')),
]
