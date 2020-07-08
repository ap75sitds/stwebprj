"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('qa.urls')),
    url(r'^polls/', include('polls.urls')),
    url('login/', include('qa.urls')),
    url('signup/', include('qa.urls')),
    #path('question/<int:qid>/', include('qa.urls')),
    path('question/', include('qa.urls')),
    url('ask/', include('qa.urls')),
    url('popular/', include('qa.urls')),
    url('new/', include('qa.urls')),
]
