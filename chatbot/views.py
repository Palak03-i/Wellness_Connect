from django.shortcuts import render

# Create your views here.
def detect_stress(message):
    if "suicide" in message.lower():
        return "High"
    elif "sad" in message.lower():
        return "Medium"
    else:
        return "Low"
