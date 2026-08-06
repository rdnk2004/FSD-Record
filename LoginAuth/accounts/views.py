from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
