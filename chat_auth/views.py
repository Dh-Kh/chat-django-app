from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import (RegisterForm, 
Change_Password, Change_Username, Change_Email)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from .sensitive_ignore import Email_one_ignore, Email_two_ignore
from django.http import HttpResponse
import pyotp
from chat_data.models import MessageHistory
totp = pyotp.TOTP("base32secret3232", interval=300)

def register(request):
    form = RegisterForm(request.POST)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            send_email("Successful registration")
            return redirect(request.GET.get('next', reverse("chat_data:dashboard")))
        else:
            messages.error(request, "Error")
    return render(request, "chat_auth/register.html", context)

def login_user(request):
    form = AuthenticationForm(data = request.POST)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', reverse("chat_data:dashboard")))
        else:
            messages.error(request, "Error")
    return render(request, "chat_auth/login_user.html", context)

@login_required
def change_password(request):
    form = Change_Password(request.user, request.POST)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            mapping_data = form.cleaned_data["verification_field"]
            if totp.verify(mapping_data):
                form.save()
                update_session_auth_hash(request, form.user)
                send_email("You have changed your password")
                return redirect(request.GET.get('next', reverse("chat_data:dashboard")))
            else:
                messages.error(request, "Failed verification")
        else:
            messages.error(request, "Error")
    return render(request, "chat_auth/change_password.html", context)

@login_required
def change_username(request):
    form = Change_Username(request.POST, instance=request.user)
    current_username = request.user.username
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            mapping_data = form.cleaned_data["username"]
            for data in MessageHistory.objects.all():
                if data.message.startswith(current_username):
                    data.message = data.message.replace(current_username, mapping_data)
                    data.save()
                
            form.save()
            send_email("You have changed your username")
            return redirect(request.GET.get('next', reverse("chat_data:dashboard")))
        else:
            messages.error(request, "Error")
    return render(request, "chat_auth/change_username.html", context)

@login_required
def change_email(request):
    form = Change_Email(request.POST, instance=request.user)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            mapping_data = form.cleaned_data["verification_field"]
            if totp.verify(mapping_data):
                form.save()
                send_email("You have changed your email")
                return redirect(request.GET.get('next', reverse("chat_data:dashboard")))
            else:
                messages.error(request, "Failed verification")
        else:
            messages.error(request, "Error")
    return render(request, "chat_auth/change_email.html", context)



def send_email(body):
    send_mail(
        'Notification',
        str(body),
        Email_one_ignore,
        [Email_two_ignore],
        fail_silently=False,
    )

def send_secret_key(request):
    send_mail("Submit action", totp.now(), Email_one_ignore, [Email_two_ignore], fail_silently=False,)
    return HttpResponse("Sending", 200)
def log_out(request):
    logout(request)
    return redirect("/chat_auth/login_user/")
