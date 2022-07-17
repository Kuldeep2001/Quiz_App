from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('show_quiz/',views.show_quiz, name='show_quiz'),
    path('show_questions/',views.show_questions, name='show_questions'),
    path('api/get_quiz',views.get_quiz, name='get_quiz'),
    path('generate_link/',views.generate_quiz_link, name='lgenerate_link'),
]