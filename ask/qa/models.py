from django.db import models
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')
    def question_on_page(self, qid):
        try :
            z = self.get(id=qid)
            ans = Answer.objects.filter(question_id=qid)
        except :
            raise Http404
        answer_to_quest = []
        for a in ans :
            answer_to_quest.append(a.text)
        fdic = {'title':z.title, 'text':z.text, 'answers':answer_to_quest}
        return fdic

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
 
    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
