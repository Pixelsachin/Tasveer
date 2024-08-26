from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def home(request):
#     return render(request, "auth/signup.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        reg_no = request.POST["reg_no"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        pass1 = request.POST["password"]
        pass2 = request.POST["password2"]

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, "auth/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "auth/signup.html")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()
        messages.success(
            request,
            "Your account has been created successfully. Please wait for admin approval.",
        )

        # subject = "New User Registration"
        # message = f"New user {username} has registered. Please approve their account."
        # from_email = settings.EMAIL_HOST_USER
        # to_email = settings.ADMIN_EMAIL
        # send_mail(subject, message, from_email, [to_email])

        return redirect("login_view")
    return render(request, "auth/signup.html")


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")  # Redirect to the index view
            else:
                messages.error(
                    request, "Your account is not active. Please contact admin."
                )
                return render(request, "auth/login.html")
        else:
            messages.error(request, "Invalid username or password")
            return redirect(request, "index")
    return render(request, "auth/login.html")


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("signup")
