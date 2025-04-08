from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile  # 👈 Only if you created a Profile model

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        gmail = request.POST['gmail']
        address = request.POST['address']
        phoneno = request.POST['phoneno']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=gmail)
        user.first_name = request.POST.get('first_name', '')
        user.save()

        # Save additional info to Profile
        Profile.objects.create(user=user, address=address, phoneno=phoneno)

        return redirect('login')
    return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login Successful {username}!")
            return redirect('/app1/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful!")
    return redirect('home')
