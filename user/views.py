from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('user:index')
    else:
        form = AuthenticationForm()
    return render(request, 'user/signin.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user:index')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('user:index')
