from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def counsellor_dashboard(request):
    if request.user.role != "counsellor":
        return HttpResponseForbidden("Access Denied")
    return render(request, "counsellor/dashboard.html")
