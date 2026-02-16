from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# ---------- LOGIN ----------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'admin':
                return redirect('/adminpanel/dashboard/')
            elif user.role == 'counsellor':
                return redirect('/counsellor/')
            elif user.role == 'student':
                return redirect('/student/')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'accounts/login.html')


# ---------- REGISTER ----------
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------- ROOT / ----------
@login_required(login_url='/login/')
def home_redirect(request):
    if request.user.role == 'admin':
        return redirect('/adminpanel/')
    elif request.user.role == 'counsellor':
        return redirect('/counsellor/')
    elif request.user.role == 'student':
        return redirect('/student/')

@login_required(login_url='/login/')
def home_redirect(request):
    user = request.user

    if user.role == 'admin':
        return redirect('/adminpanel/')
    elif user.role == 'counsellor':
        return redirect('/counsellor/')
    elif user.role == 'student':
        return redirect('/student/')
    else:
        # SAFETY FALLBACK (VERY IMPORTANT)
        return redirect('/login/')

