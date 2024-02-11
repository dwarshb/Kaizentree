from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if 'login' in request.POST:
            user = authenticate(request, username=username, password=password)
        elif 'signup' in request.POST:
            user = User.objects.create_user(username=username, email=username, password=password)
            
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

