from django.shortcuts import render, redirect
from authentication.forms import  SignupForm , UploadProfilePhotoForm

from django.contrib.auth import authenticate, login, logout

## page de connection
from django.views.generic import View
from django.conf import settings


def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def upload_profile_photo(request):
    form = UploadProfilePhotoForm()
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

