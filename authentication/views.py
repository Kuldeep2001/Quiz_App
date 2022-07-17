from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from quiz_app import settings
from django.core.mail import EmailMessage,send_mail
from .tokens import generate_token
from django.utils.encoding import force_bytes,force_str
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from .models import *
def index(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.user.is_authenticated:
        messages.error(request, 'You have already logged in \n Please logout first then try again')
        return render(request,'index.html')

    if request.method == 'POST':
        fname = request.POST.get('fname','')
        lname = request.POST.get("lname",'')
        email = request.POST.get("email",'')
        uname = request.POST.get("username",'')
        pass1 = request.POST.get("password1",'')
        pass2 = request.POST.get("password2",'')

        if User.objects.filter(username=uname):
            messages.error(request, 'Username already exists, Please try some other username')
            return redirect('/authenticate/register')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered, Please login')
            return redirect('/authenticate/register')

        if pass1 != pass2:
            messages.error(request, 'Password didn\'t matched')
            return redirect('/authenticate/register')

        if not uname.isalnum():
            messages.error(request, 'UserName can only contain alphanumeric characters')
            return redirect('/authenticate/register')

        user = User.objects.create_user(first_name = fname,last_name = lname,username = uname, email = email,password = pass1)
        user.is_active = False
        user.save()
        messages.success(request, 'Account created successfully. Check the Confirmation link in your email')


        # Welcome Email
        subject = "Welcome to the admin panel of Quiz-App"
        message = "Hello " + user.first_name + "!!\nWelcome to the Quiz-App!!\n\nPlease verify you Email-ID to activate your account!!\n\nThank you"

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)

        # Email Address Confirmation mail
        current_site = get_current_site(request)
        email_subject = "Confirm you email-account for Quiz-Admin"
        message2 = render_to_string('email_confirmation.html',{
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        print(message2)
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently = True
        email.send()


        return redirect('/authenticate/login')
    # return HttpResponse('User')
    return render(request,'authentication/register.html')

def signin(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        messages.success(request, 'You have already logged in')
        return redirect('/')

    if request.method == 'POST':
        usename = request.POST.get("username",'')
        pass1 = request.POST.get("password",'')

        user = authenticate(username=usename, password=pass1)
        print(user)

        if user is not NONE:
            login(request,user)
            messages.success(request, 'Logged In successfully')
            return render(request, 'authentication/index.html')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('/authenticate/login')
    return render(request, 'authentication/login.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not NONE and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, 'Email Confirmation done')
        return redirect('/')
    else:
        return render(request, 'activation_failed.html')