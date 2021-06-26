from django.shortcuts import render, HttpResponse


# add views to different blog posts here
def blog_home(request):
    return render(request, 'blog/home.html')


def blog_post(request, slug):
    return HttpResponse(f"This is blogpost named {slug} which we fetch from the db")


