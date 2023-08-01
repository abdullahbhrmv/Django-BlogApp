from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "account/login.html")
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Invalid username or password"
            })


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "account/register.html")

    def post(self, request):
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html", {
                "error": "Passwords do not match",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
        elif User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {
                "error": "This username already exists",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
        elif User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {
                "error": "This email already exists",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
        else:
            user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
            user.save()
            return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
