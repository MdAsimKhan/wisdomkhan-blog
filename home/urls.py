from home import views
from django.contrib import admin
from django.urls import path,include

# this is the home page of the website
# /about etc to view different views. These are like the nav buttons on home pg navbar
# this path directs it to home app where we have everything what is to be shown at home page
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('contribute', views.contribute, name='contribute'),
]