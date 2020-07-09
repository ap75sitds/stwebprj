from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Question, Answer

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