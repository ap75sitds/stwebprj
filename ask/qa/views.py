from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Question, Answer
from .forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('Firstclass App')

def one_question(request, *args, **kwargs):
    qid = kwargs['qid']
    resp = Question.objects.question_on_page(qid)
    return render(request, 'qa/index.html', resp)

def post_ten_page(request):
    posts = Question.objects.new() # metod "new" from models.py
    limit = int(request.GET.get('limit', 10))
    number_page = int(request.GET.get('page', 1)) # return 1 from URL (/?page=1)
    paginator = Paginator(posts, limit)
    page = paginator.page(number_page)
    return render(request, 'qa/pages.html', {
        'page':page, 
        'paginator':page.object_list,
        'link':'/question/',
        })

def popular_qst(request):
    posts = Question.objects.popular() # metod "popular" from models.py
    limit = int(request.GET.get('limit', 10))
    number_page = int(request.GET.get('page', 1)) # return 1 from URL (/?page=1)
    paginator = Paginator(posts, limit)
    page = paginator.page(number_page)
    return render(request, 'qa/popular.html', {
        'page':page, 
        'paginator':page.object_list,
        'link':'/question/',
        })

def ask_new(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.added_at = timezone.now()
            quest.author = request.user
            quest.likes = request.user
            quest.save()
            return redirect('one_question', qid=quest.pk) # one_question from usrl.py - name
    else:
        form = AskForm()
    return render(request, 'qa/forms.html', {'form':form})

def answer_new(request, *args, **kwargs):
    qid = kwargs['qid']
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.added_at = timezone.now()
            ans.author = request.user
            ans.save()
            return redirect('one_question', qid=kwargs['qid']) # one_question from usrl.py - name
    else:
        form = AnswerForm()
    resp = Question.objects.question_on_page(qid)
    #print(form)
    resp['form'] = form
    resp['qid'] = qid
    return render(request, 'qa/index.html', resp)