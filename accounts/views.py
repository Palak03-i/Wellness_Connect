from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# ---------- LOGIN ----------

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'student':
                return redirect('student:student_dashboard')
            elif user.role == 'counsellor':
                return redirect('counsellor:counsellor_dashboard')
            elif user.role == 'admin':
                return redirect('admin:admin_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


# ---------- REGISTER ----------
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------- ROOT / ----------
@login_required
def home_redirect(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'counsellor':
        return redirect('counsellor_dashboard')
    elif request.user.role == 'student':
        return redirect('student_dashboard')

@login_required
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

@login_required
def counsellor_dashboard(request):
    return render(request, 'counsellor/dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return redirect('accounts:login')
    return render(request, 'student/student_dashboard.html')

@login_required
def home_redirect(request):
    user = request.user

    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'counsellor':
        return redirect('counsellor_dashboard')
    elif user.role == 'student':
        return redirect('student:student_dashboard')
    else:
        # SAFETY FALLBACK (VERY IMPORTANT)
        return redirect('accounts:login')

