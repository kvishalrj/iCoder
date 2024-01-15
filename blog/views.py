from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from django.views import View


class BlogHomeView(View):
    def get(self, request):
        allPosts = Post.objects.all()
        recentPosts = [post for post in allPosts]
        recentPosts.sort(key=self.cal_hours)
        context = {'allPosts': allPosts, 'recentPosts': recentPosts}
        return render(request, 'blog/blogHome.html', context)

    @staticmethod
    def cal_hours(post):
        given_datetime = datetime.strptime(str(post.timeStamp), "%Y-%m-%d %H:%M:%S%z")
        current_time = timezone.now()
        time_difference = current_time - given_datetime
        hours_difference = time_difference.total_seconds() / 3600
        return hours_difference

class BlogPostView(View):
    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        post.views = post.views + 1
        post.save()
        comments = BlogComment.objects.filter(post=post, parent=None)
        replies = BlogComment.objects.filter(post=post).exclude(parent=None)
        reply_dict = {}

        for reply in replies:
            if reply.parent.sno not in reply_dict.keys():
                reply_dict[reply.parent.sno] = [reply]
            else:
                reply_dict[reply.parent.sno].append(reply)

        context = {'post': post, 'comments': comments, 'replyDict': reply_dict, 'user': request.user}
        return render(request, 'blog/blogPost.html', context)

class PostCommentView(View):
    def post(self, request):
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
