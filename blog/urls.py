from . import views
from django.contrib import admin
from django.urls import path,include


# this is the blog page of the website
urlpatterns = [
    path('', views.blog_home, name='blogHome'),
    # <str:slug>captures any string types after the /blog
    path('<str:slug>', views.blog_post, name='blogPost'),
]