from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login

# Create your views here.
def registerUsers(request):
    if request.user.is_authenticated:
        return redirect('book:index')
    
    if request.method == 'POST':
       username = request.POST['username']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       password = request.POST['password']
       
       User.objects.create_user(
           username = username, 
           first_name= first_name, 
           last_name= last_name, 
           email= email, 
           password= password, 
        )
       return redirect('users:login')
       
    else:
        return render(
            request,
            'users/register.html'
        )
        
        
def login(request):
    if request.user.is_authenticated:
        return redirect('book:index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user_ = User.objects.filter(username=username).first()
        
        if user_:
            user = authenticate(username=username, password=password)
            
            if user:
                auth_login(request, user)
                return redirect('book:index')
            else:
                messages.add_message(request, messages.ERROR, "Username or Password is Incorrect")
            
                return render(
                    request,
                    'users/login.html'
                ) 
        else:
            return redirect('users:register')
       
    else:
        return render(
            request,
            'users/login.html'
        )
        

def user_logout(request):
    logout(request)
    return redirect('users:login')