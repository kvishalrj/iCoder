from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# custom calculation by function
def calHours(post):
    # Given datetime
    given_datetime = datetime.strptime(str(post.timeStamp), "%Y-%m-%d %H:%M:%S%z")
    # Current time
    current_time = timezone.now()
    # Calculate the time difference
    time_difference = current_time - given_datetime
    # Convert the time difference to hours
    hours_difference = time_difference.total_seconds() / 3600

    return hours_difference

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    recentPosts = [post for post in allPosts]
    recentPosts.sort(key=calHours)
    context = {'allPosts' : allPosts, 'recentPosts' : recentPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys(): 
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    
    context = {'post':post, 'comments':comments, 'replyDict':replyDict, 'user':request.user}
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method=='POST':
        comment = request.POST.get("comment")
        slug = request.POST.get("postSlug")
        if comment=="":
            messages.error(request, "Please write a comment")
            return redirect(f"/blog/{slug}")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno=="":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/blog/{slug}")
    
        
