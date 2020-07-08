from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, Answer

def test(request, *args, **kwargs):
    
    return HttpResponse('Firstclass App')

def one_question(request, *args, **kwargs):
    qid = kwargs['qid']
    resp = Question.objects.question_on_page(qid)
    return render(request, 'qa/index.html', resp)