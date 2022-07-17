import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import random
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import generate_token

def index(request):
    return render(request, 'quiz_create/questions.html')

def add_questions(request):
    return render(request, 'quiz_create/add_question.html')

def show_quiz(request):
    quiz = Quiz.objects.all()
    quiz = quiz[0]

    quiz = quiz.get_questions()

    ques = []
    for q in quiz:
        ques.append({
            'image': q.question.image,
            'question': q.question.question,
            'options': q.question.get_options()
        })
    # print(ques[0]['question'])
    params = {
        'quiz':quiz
    }

    # return HttpResponse('Hello')
    return render('quiz_create/show_quiz.html',params)

def generate_quiz_link(request):
    domain = get_current_site(request)
    print(domain)
    domain = domain.domain
    quiz = Quiz.objects.all()
    quiz = quiz[0]
    print(quiz)
    uid = urlsafe_base64_encode(force_bytes(quiz.pk))
    token = generate_token.make_token(quiz)
    link = "http://" + domain + "/quiz_interface/validate/" + uid + "/" + token
    print(link)
    return HttpResponse('Link generated')

def show_questions(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not allowed to access this page')
        return redirect('/')

    cats = Category.objects.all()
    for cat in cats:
        print(cat)

    params = {
        'categories':cats
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
