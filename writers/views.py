from django.shortcuts import render
from django.contrib.auth.models import User
from writers.models import Writer
from blog.models import Post

# Create your views here.
def writers(request):
    users = Writer.objects.all()
    context = {'users' : users}
    return render(request, 'writers/writers.html', context)

def userView(request, slug):
    writer = Writer.objects.filter(firstName=slug).first()
    posts = Post.objects.filter(author=writer.firstName)
    context = {'writer' : writer, 'posts' : posts}
    return render(request, 'writers/userView.html', context)

def profileView(request, slug):
    writer = Writer.objects.filter(firstName=slug).first()
    posts = Post.objects.filter(author=writer.firstName)
    context = {'writer' : writer, 'posts' : posts}
    return render(request, 'writers/profile.html', context)


