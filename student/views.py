from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    if request.user.role != "student":
        return HttpResponseForbidden("Access Denied")
    return render(request, "student/dashboard.html")
