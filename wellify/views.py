from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! My first Django App is working 🎉")
