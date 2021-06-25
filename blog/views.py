from django.shortcuts import render, HttpResponse


def home(index):
    return HttpResponse("Welcome to the Home page.")
