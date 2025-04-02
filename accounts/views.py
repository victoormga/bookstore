from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import Customuser
from django.contrib.auth.decorators import login_required

# Log In view
def log_in(request):
    return render(request, 'accounts/login.html')

# Sign Up view
def sign_up(request):
    template_data = {'title' : 'Sign Up'}

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', template_data)
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', template_data)

# Log Out view
@login_required
def log_out(request):
    logout(request)
    return redirect('home')