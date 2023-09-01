from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse



@login_required(login_url="/login/")
def home(request):
    return render(request, 'main/home.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration/login.html')  # Redirect to login page

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(username=username, password=password)
 
        if user is not None:

            login(request, user)
            return render(request, 'main/home.html')

        else:

            messages.error(request, 'Invalid Credentials')
            return render(request, 'registration/login.html', {'username': username})

    else:
        
        return render(request, 'registration/login.html')
    
def profile(request):

    user_email = request.user.email

    return render(request, 'main/profile.html', {'user_email':user_email})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def user_info_update(request):
    if request.method == "POST" and is_ajax(request=request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        
        user = request.user  
        user.username = username
        user.email = email
        user.save()

        return JsonResponse({"message": "Data updated successfully."})
    else:
        return JsonResponse({"message": "Invalid request."}, status=400)
