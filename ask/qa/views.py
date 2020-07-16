from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sessions.models import Session

from django.utils import timezone

from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignUpForm

def test(request, *args, **kwargs):
    return HttpResponse('Firstclass App')

def logout(request):
    Session.objects.all().delete()
    sessid = request.COOKIES.get('sessid')
    print(sessid)
    if sessid is not None:
        Session.objects.delete(key=sessid)
    return redirect('main')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
        return redirect('main')
    else:
        form = AuthenticationForm()
        return render(request, 'qa/login.html', {'form':form})

def signup(request):
    Session.objects.all().delete()
    if request.method == 'POST':
        print('request.POST',request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            hashpass = form.save(commit=False) #before real save to db
            new_user = form.cleaned_data.get('username')
            password_open = form.cleaned_data.get('password')
            password = make_password(password_open) #create HASH password
            hashpass.password = password
            hashpass.save()
            form.save_m2m()
        user = authenticate(username=new_user, password=password_open)
        if user is not None:
            login(request, user)
        else:
            print('pizdec', username, password)    
        return redirect('main')
    else:
        form = SignUpForm()
        return render(request, 'qa/signup.html', {'form':form})

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
        'user':request.user,
        'coc':request.COOKIES,
        'page':page, 
        'paginator':page.object_list,
        'link':'/question/',
        })

def popular_qst(request):
    if request.user.is_authenticated:
        posts = Question.objects.popular() # metod "popular" from models.py
        limit = int(request.GET.get('limit', 10))
        number_page = int(request.GET.get('page', 1)) # return 1 from URL (/?page=1)
        paginator = Paginator(posts, limit)
        page = paginator.page(number_page)
        return render(request, 'qa/popular.html', {
            'request':request.user,
            'post':request.GET,
            'page':page, 
            'paginator':page.object_list,
            'link':'/question/',
            })
    else:
        return redirect('login')

def ask_new(request):
    alex_pass = User.objects.get(pk=1).password
    alex_name = User.objects.get(pk=1).username
    print(check_password('123', alex_pass))
    print('Xheck user - ', alex_name, alex_pass)
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.added_at = timezone.now()
            quest.author = request.user
            #quest.likes = request.user
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