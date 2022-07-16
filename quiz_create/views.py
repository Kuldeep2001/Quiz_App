from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Question
import random

def index(request):
    return render(request, 'quiz_create/questions.html')

def add_questions(request):
    return render(request, 'quiz_create/add_question.html')

def show_questions(request):
    ques = Question.objects.all()

    params = {
        'questions':ques
    }

    # return HttpResponse('Hello')
    return render(request, 'quiz_create/show_questions.html', params)

def get_quiz(request):
    try:
        questions_objs = Question.objects.all()
        random.shuffle(list(questions_objs))
        data = []
        for question in questions_objs:
            data.append({
                "category":question.category.category_name,
                "question":question.question,
                "marks": question.marks
            })
        payload = {
            "status":True,
            "data":data
        }
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something Went Wrong")
