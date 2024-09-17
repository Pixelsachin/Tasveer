from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError

# from django.conf import settings
from pehchan import settings
from .models import img_load, userprofile
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, ProfileForm
from django.utils import timezone
from datetime import timedelta

# notifiction
from webpush import send_user_notification


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        # reg_no = request.POST["reg_no"]
        # phone = request.POST["phone"]
        email = request.POST["email"].lower()
        pass1 = request.POST["password"]
        pass2 = request.POST["password2"]

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, "auth/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "auth/signup.html")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = True
        myuser.save()
        messages.success(
            request,
            "Your account has been created successfully.login",
        )

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
                return redirect("index")
            else:
                messages.error(
                    request, "Your account is not active. Please contact admin."
                )
                return render(request, "auth/login.html")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login_view")
    return render(request, "auth/login.html")


# @login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "signup first to get acces  to dashboard")
        return redirect("signup")

    name = request.user.username
    images = img_load.objects.all()
    delete_expired_images()
    return render(request, "index.html", {"images": images, "name": name})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("welcome")


@login_required
def img_handle(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save(commit=False)
            img_instance.user = (
                request.user
            )  # Associate the logged-in user with the image
            img_instance.save()
            return redirect("index")

    else:
        form = ImageUploadForm()
    return render(request, "index.html", {"form": form})


def welcome(request):
    return render(request, "welcome/welcome.html")


def delete_expired_images():
    expiration_time = timezone.now() - timedelta(minutes=1)
    expired_images = img_load.objects.filter(uploaded_at__lt=expiration_time)
    for image in expired_images:
        image.image.delete(save=True)
        image.delete()
    return


def aboutus(request):
    return render(request, "sections/about.html")


@login_required
def profile(request):
    users = User.objects.all()

    return render(request, "sections/user/profile.html", {"users": users})


@login_required
def userpf(request):
    profiles, created = userprofile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfileForm(instance=profiles)
    return render(
        request, "sections/user/userpfile.html", {"form": form, "user": request.user}
    )


# Create your views here.
def testing(request):
    payload = {"head": "Welcome!", "body": "Hello World"}
    send_user_notification(user=request.user, payload=payload, ttl=1000)
    webpush = {"group": "aman"}
    return render(request, "testing.html", {"webpush": webpush})
