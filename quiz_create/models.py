from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    def get_questions(self):
        return Question.objects.filter(category = self)

class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'quiz_create/images', null=True, blank=True, default="")
    marks = models.IntegerField(default=4)

    def __str__(self):
        return self.question

    def get_options(self):
        return Answer.objects.filter(question = self)

class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class Quiz(BaseModel):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=50, default='')
    number_of_questions = models.IntegerField(default=0)
    time = models.IntegerField(help_text="duration of the quiz", default=120)

    def __str__(self):
        return (self.name + ' ' + self.title)

    def get_questions(self):
        return Quiz_Questions.objects.filter(quiz = self)

class Quiz_Questions(BaseModel):
    quiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question_quiz', on_delete=models.CASCADE)