from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'users/index.html')

def register(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')