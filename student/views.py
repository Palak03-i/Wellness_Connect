from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required(login_url='accounts:login')
def student_dashboard(request):
    if request.user.role != 'student':
        return redirect('accounts:login')
    return render(request, 'student/dashboard.html')
