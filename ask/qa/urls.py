from django.conf.urls import url
from django.urls import path
from . import views

#views.one_question

urlpatterns = [
    #url(r'^$', views.test),
    path('question/<int:qid>/', views.answer_new, name='one_question'),
    path('popular/', views.popular_qst),
    path('ask/', views.ask_new),
    path('new/', views.post_ten_page),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.post_ten_page, name='main')
]
