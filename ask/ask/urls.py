from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('qa.urls')),
    url('', include('qa.urls')),
    url(r'^polls/', include('polls.urls')),
    #url('login/', include('qa.urls')),
    #url('signup/', include('qa.urls')),
    #url('ask/', include('qa.urls')),
    #path('question/', include('qa.urls')),

    #url('popular/', include('qa.urls')),
    #url('new/', include('qa.urls')),
]
