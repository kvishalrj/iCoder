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
    if request.user.username==slug:
        writer = Writer.objects.filter(firstName=slug).first()
        posts = Post.objects.filter(author=writer.firstName)
        context = {'writer' : writer, 'posts' : posts}
        return render(request, 'writers/profile.html', context)

def editProfile(request, slug):
    writer = Writer.objects.filter(firstName=slug).first()
    context = {'writer' : writer}
    return render(request, 'writers/editProfile.html', context)

def profileUpdate(request, slug):
    if request.method=='POST':
        bio = request.POST.get('bio')
        picture = request.FILES.get('picture', 'blog/user/default_user.png')
        profile = Writer.objects.filter(firstName=slug).first()
        if bio!="":
            profile.bio = bio
        if picture:
            profile.userImage = picture
        profile.save()
        messages.success(request, 'Your profile has been successfully updated.')
        posts = Post.objects.filter(author=profile.firstName)
        context = {'writer' : profile, 'posts' : posts}
        return render(request, 'writers/profile.html', context)

def newBlog(request, slug):
    return render(request, 'writers/tiny.html')

def deleteBlog(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.delete()
    messages.success(request, 'Your post has been deleted successfully')
    return redirect(request.META['HTTP_REFERER'])

def editBlog(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'writers/editBlog.html', context)

def blogUpdate(request, slug):
    if request.method=='POST':
        ptitle = request.POST.get('title')
        ppicture = request.FILES.get('picture')
        pslug = request.POST.get('slug')
        pcontent = request.POST.get('content')
        post = Post.objects.filter(slug=slug).first()
        post.title = ptitle
        post.slug = pslug
        post.content = pcontent
        if ppicture:
            post.postImage = ppicture
        post.save()
        messages.success(request, 'Your post has been successfully updated.')
        previous_url = request.META.get('HTTP_REFERER')
        if previous_url:
            return redirect(previous_url)




    

    
    

