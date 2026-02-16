from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def admin_dashboard(request):
    if request.user.role != "admin":
        return HttpResponseForbidden("Access Denied")
    return render(request, "adminpanel/dashboard.html")
