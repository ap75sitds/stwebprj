from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.test),
    path('<int:qid>/', views.one_question),
    path('popular/', views.popular_qst),
    path('', views.post_ten_page)
]
