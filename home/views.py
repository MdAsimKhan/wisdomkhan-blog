from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        if len(name) < 2 or len(email) < 3 or len(msg) < 10:
            messages.error(request, 'Please fill the form correctly!')
        else:
            newObj = Contact(name=name, email=email, msg=msg)
            newObj.save()
            messages.success(request, 'Message sent successfully!')
    return render(request, 'home/contact.html')


def contribute(request):
    return render(request, 'home/contribute.html')
