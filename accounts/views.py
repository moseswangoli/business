from django.http import HttpResponse
from django.core.management import call_command

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔥 Redirect based on role
            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_receptionist:
                return redirect('/receptionist/dashboard/')
            else:
                return redirect('/')  # fallback

        else:
            error = "Invalid credentials"

    return render(request, "login.html", {"error": error})