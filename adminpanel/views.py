from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required(login_url='accounts:login')
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('accounts:login')
    return render(request, 'adminpanel/dashboard.html')
