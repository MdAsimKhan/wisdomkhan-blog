from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Contribute


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
            messages.success(request, "Message sent successfully!")
    return render(request, 'home/contact.html')


def contribute(request):
    return render(request, 'home/contribute.html')


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        post = Contribute.objects.none()
    else:
        postTitle = Contribute.objects.filter(title__icontains=query)
        postText = Contribute.objects.filter(text__icontains=query)
        post = postTitle.union(postText)
    if post.count() == 0:
        messages.warning(request, 'Nothing found')
    param = {'post': post, 'query': query}
    return render(request, 'home/search.html', param)


def login(request):
    return render(request, 'home/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        newuser = User.objects.create_user(username, email, password)
        newuser.first_name = fullname
        newuser.save()
        messages.success(request, 'Your account has been created successfully')
    else:
        return HttpResponse('Bad Request')
    return render(request, 'home/signup.html')

