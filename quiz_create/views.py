from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Question,Answer

def index(request):
    return render(request, 'quiz_create/questions.html')

def add_questions(request):
    return render(request, 'quiz_create/add_question.html')

def show_questions(request):
    cats = Category.objects.all()
    ques = Question.objects.all()

    params = {
        'questions':ques
    }
    for q in cats:
        print(q.get_questions())
    # return HttpResponse('Hello')
    return render(request, 'quiz_create/show_questions.html', params)