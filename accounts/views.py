from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .forms import ProfileForm, CustomUserCreationForm
from .models import UserProfile

# Create your views here.

def signup(request):
    context = {'form': CustomUserCreationForm}
    if request.method == 'POST':
        form_filled = CustomUserCreationForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save(commit = False)

            username = form_filled.cleaned_data.get('username')
            password = form_filled.cleaned_data.get('password1')

            # Authentiacate
            user = authenticate(username = username, password = password)
            
            user = form_filled.save()

            UserProfile.objects.create(user_id = user.id)

            login(request, user)
            return redirect('update_profile')

        else:
            return render(request, 'signup.html', {'form': form_filled})

    return render(request, 'signup.html', context)

def signin(request):
    # if request.user.is_authenticated:
    #     return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(username = username, password = password)
        if user is not None:
            # login takes request and the user associated
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'form': AuthenticationForm(request.POST)})
    
    else:
        return render(request, 'signin.html', {'form': AuthenticationForm})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')


def update_profile(request):
    
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None, instance=profile)
    context = {'form': form} 

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'update_profile.html', context)


def profile(request):

    user = request.user
    profile = user.userprofile     
    context = {'profile': profile}

    return render(request, 'profile.html', context)


