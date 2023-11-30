from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from writers.models import Writer
from blog.models import Post
from django.contrib import messages

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
    if request.method=='POST':
        bio = request.POST.get('bio')
        picture = request.FILES.get('picture', 'blog/user/default_user.png')
        profile = Writer.objects.filter(firstName=slug).first()
        profile.bio = bio
        if picture:
            profile.userImage = picture
        profile.save()
        messages.success(request, 'Your profile has been successfully updated.')
        posts = Post.objects.filter(author=profile.firstName)
        context = {'writer' : profile, 'posts' : posts}
        return render(request, 'writers/profile.html', context)
    
    elif request.user.username==slug:
        writer = Writer.objects.filter(firstName=slug).first()
        posts = Post.objects.filter(author=writer.firstName)
        context = {'writer' : writer, 'posts' : posts}
        return render(request, 'writers/profile.html', context)

def editProfile(request, slug):
    writer = Writer.objects.filter(firstName=slug).first()
    context = {'writer' : writer}
    return render(request, 'writers/editProfile.html', context)

def newBlog(request, slug):
    return render(request, 'writers/tiny.html')

    

    
    


