from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='authentication'),
    path('register/',views.register, name='register'),
    # path('adduser/',views.adduser,name = "adduser"),
    path('login/',views.signin, name='login'),
    path('logout/',views.signout, name='signout'),
    # path('submit/',views.submit,name = 'submit'),
    path('activate/<uidb64>/<token>', views.activate, name="activate")
]