from pickle import NONE
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from quiz_create.models import Quiz
from quiz_create.tokens import generate_token

# Create your views here.

def index(request):
    return HttpResponse('Hello')

def show_quiz(request,uid):
    quiz = Quiz.objects.filter(uid = uid)
    quiz = quiz[0].get_questions()
    print(quiz)
    for qz in quiz:
        print(qz.question)

    # for q in quiz:
    #     ques.append({
    #         'image': q.question.image,
    #         'question': q.question.question,
    #         'options': q.question.get_options()
    #     })
    params = {
        'quiz':quiz
    }

    # return HttpResponse('Hello')
    return render('quiz_interface/show_quiz.html',params)

def quiz(request,uidb64,token):
    # http://127.0.0.1:8000/authenticate/activate/MjA/b8ptqe-546c64e07b3deb64aab3a20e47d16858
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myquiz = Quiz.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Quiz.DoesNotExist):
        myquiz = None

    if myquiz is not NONE and generate_token.check_token(myquiz, token):
        messages.success(request, 'Link validated successfully')
        return HttpResponse('Validate')
        # return redirect('/quiz_interface/show_quiz/'+uid)
    else:
        return render(request, 'activation_failed.html')