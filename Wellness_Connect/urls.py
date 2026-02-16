from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('student/', include('student.urls')),
    path('counsellor/', include('counsellor.urls')),
    path('adminpanel/', include('adminpanel.urls')),
    path('booking/', include('booking.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('assessment/', include('assessment.urls')),
    
]
