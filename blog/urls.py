from . import views
from django.contrib import admin
from django.urls import path,include


# this is the blog page of the website
urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    # <str:slug>captures any string types after the /blog
    path('<str:slug>', views.blogPost, name='blogPost'),
]