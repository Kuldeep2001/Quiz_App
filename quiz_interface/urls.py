from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='quizPage'),
    path('validate/<uidb64>/<token>', views.quiz, name="validate_link"),
    path('show_quiz/<uid>', views.show_quiz, name="show_quiz")
]