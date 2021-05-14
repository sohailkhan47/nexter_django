from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check for username 
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('signup')
                else:
                    # Looks good
                    
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name)
                    # Code to Login the user directly after register
                    """
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
                    """
                    # code to login user directly ends here
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:   
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')