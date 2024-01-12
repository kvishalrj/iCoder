from django.utils import timezone
import pytz
from django.http import HttpResponseRedirect
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
        profile = Writer.objects.filter(firstName=slug).first()
        bio = request.POST.get('bio', profile.bio)
        picture = request.FILES.get('picture', profile.userImage)
        profile.bio  = bio
        profile.userImage = picture
        profile.save()
        messages.success(request, 'Your profile has been successfully updated.')
        posts = Post.objects.filter(author=profile.firstName)
        context = {'writer' : profile, 'posts' : posts}
        return render(request, 'writers/profile.html', context)

def newBlog(request, slug):
    author = {'name' : slug}
    return render(request, 'writers/newBlog.html', author)

def saveNewBlog(request, slug):
    if request.method=='POST' and request.user.username==slug:

        # Set the desired timezone (replace 'America/New_York' with your preferred timezone)
        desired_timezone = pytz.timezone('Asia/Kolkata')

        # Get the current time in the specified timezone
        current_time = timezone.now().astimezone(desired_timezone)

        # Format the current time
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S%z')

        # Print the result (optional)
        print(formatted_time)

        ptitle = request.POST.get('title')
        ppicture = request.FILES.get('picture')
        pcontent = request.POST.get('content')
        pauthor = slug
        pslug = request.POST.get('slug')
        ptimestamp = formatted_time

        Post.objects.create(title=ptitle, postImage=ppicture,content=pcontent, author=pauthor, slug=pslug, timeStamp=ptimestamp)
        
        messages.success(request, 'Your post has been uploaded successfully')

        return profileView(request, slug)
        
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
        post = Post.objects.filter(slug=slug).first()
        ptitle = request.POST.get('title', post.title)
        ppicture = request.FILES.get('picture', post.postImage)
        pcontent = request.POST.get('content', post.content)
        pslug = request.POST.get('slug', post.slug)
        post.title = ptitle
        post.slug = pslug
        post.content = pcontent
        post.postImage = ppicture
        post.save()
        messages.success(request, 'Your post has been successfully updated.')
        
        return redirect(f'/writers/profile/{post.author}')




    

    
    


