from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login/')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print("Username: ", username)
        print("Password: ", password)
        print("User:", user)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect('/')  # Replace 'dashboard' with your actual dashboard URL name
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')