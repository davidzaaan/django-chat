from django.shortcuts import redirect, render
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username'].lower().strip()

        # Redirecting the user to the Chat Index page to select a Room to join...
        return redirect('index', username)
        
    return render(request, 'users/index.html')


def logout_user(request):
    messages.success(request, 'Logged out successfully')
    return redirect('login')