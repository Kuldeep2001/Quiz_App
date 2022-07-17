from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)

admin.site.register(Quiz_Questions)
class Quiz_QuestionsAdmin(admin.StackedInline):
    model = Quiz_Questions

class QuizAdmin(admin.ModelAdmin):
    inlines = [Quiz_QuestionsAdmin]

admin.site.register(Quiz , QuizAdmin)