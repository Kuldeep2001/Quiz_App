from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='users'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
]