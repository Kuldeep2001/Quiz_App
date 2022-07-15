from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add_questions/',views.add_questions, name='add_questions'),
    path('show_questions/',views.show_questions, name='show_questions'),
]