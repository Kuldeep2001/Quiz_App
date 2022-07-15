from email.policy import default
from django.db import models
import uuid

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
    image = models.ImageField(upload_to = 'quiz_create/images', default="")
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