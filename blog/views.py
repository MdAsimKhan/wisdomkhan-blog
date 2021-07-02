from django.shortcuts import render
from blog.models import Contribute


# add views to different blog posts here
def blogHome(request):
    posts = Contribute.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blogHome.html', context)


# slug here is used in urls.py
def blogPost(request, slug):
    post = Contribute.objects.filter(slug=slug)[0]
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)


