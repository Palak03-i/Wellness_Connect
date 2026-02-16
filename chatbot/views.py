from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def detect_stress(message):
    if "suicide" in message.lower():
        return "High"
    elif "sad" in message.lower():
        return "Medium"
    else:
        return "Low"
@login_required
def dashboard(request):
    return render(request, 'chatbot/dashboard.html')