
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserLoginForm, UserLogoutForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'user registred successfully', 'success')
            return redirect('home')
    else:

        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('home')

            else:
                messages.error(request, 'username or password is wrong', 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, 'logged out successfully', 'success')
    return redirect('home')


