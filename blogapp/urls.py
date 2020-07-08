"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from .import views
#the url till this time will already have blog appended at the end of it
urlpatterns = [
    path('', views.bloghome,name="bloghome"),
    #very important as postcomment will be considered as a slug if written below <str:slug>
    path('postcomment',views.postcomment,name='postcomment'),
    #path('<str:slug>',views.blogpost,name="blogpost"),#url will be of the form server/blog(somestring)
    path('<str:slug>',views.blogpost,name="blogpost"),
]