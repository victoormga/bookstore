from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

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
            return redirect('login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', template_data)

# Log In view
def log_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {
            'form': AuthenticationForm()
        })
    else:
        form = AuthenticationForm(data=request.POST)  # Autenticación integrada

        if form.is_valid():
            user = form.get_user()  # Obtiene el usuario autenticado
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {
                'form': form,
                'error': 'Username or password is incorrect'
            })

# Log Out view
@login_required
def log_out(request):
    logout(request)
    return redirect('home')