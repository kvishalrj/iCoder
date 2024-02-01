from django.utils import timezone
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from writers.models import Writer
from blog.models import Post
from django.contrib import messages
from django.views import View
import cloudinary.uploader  # for uploading images
import cloudinary.api      # for other Cloudinary API calls


class WritersView(View):
    def get(self, request):
        users = Writer.objects.all()
        context = {'users' : users}
        return render(request, 'writers/writers.html', context)

class UserView(View):
    def get(self, request, slug):
        writer = Writer.objects.filter(username=slug).first()
        posts = Post.objects.filter(username=writer.username)
        context = {'writer' : writer, 'posts' : posts}
        return render(request, 'writers/userView.html', context)

class ProfileView(View):
    def get(self, request, slug):
        if request.user.username==slug:
            writer = Writer.objects.filter(username=slug).first()
            posts = Post.objects.filter(username=writer.username)
            context = {'writer' : writer, 'posts' : posts}
            return render(request, 'writers/profile.html', context)
        
class EditProfileView(View):
    def get(self, request, slug):
        writer = Writer.objects.filter(username=slug).first()
        context = {'writer' : writer}
        return render(request, 'writers/editProfile.html', context)

    def post(self, request, slug):
        profile = Writer.objects.filter(username=slug).first()
        bio = request.POST.get('bio', profile.bio)
        picture = request.FILES.get('picture', profile.userImage)

        # Upload the file to Cloudinary
        upload_result = cloudinary.uploader.upload(
            picture,
            public_id=f"iCoder/media/users/{slug}",
            overwrite=True,
            resource_type="image"
        )

        # save the Cloudinary URL to the user's profile
        cloudinary_url = upload_result['secure_url']

        profile.bio  = bio
        profile.userImage = cloudinary_url
        profile.save()
        
        messages.success(request, 'Your profile has been successfully updated.')

        return redirect(f'/writers/profile/{slug}')

class NewBlogView(View):
    def get(self, request, slug):
        writer = Writer.objects.filter(username=slug).first()
        writer = {'writer' : writer}
        return render(request, 'writers/newBlog.html', writer)
    
    def post(self, request, slug): 
        desired_timezone = pytz.timezone('Asia/Kolkata')
        current_time = timezone.now().astimezone(desired_timezone)
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S%z')

        writer = Writer.objects.filter(username=slug).first()

        ptitle = request.POST.get('title')
        pslug = request.POST.get('slug')
        pcontent = request.POST.get('content')
        ppicture = request.FILES.get('picture')

        if ppicture:
            if ppicture.size > 0:
                # Upload the file to Cloudinary
                upload_result = cloudinary.uploader.upload(
                    ppicture,
                    public_id=f"iCoder/media/posts/{pslug}",
                    overwrite=True,
                    resource_type="image"
                )

                # save the Cloudinary URL to the user's profile
                cloudinary_url = upload_result['secure_url']
            else:
                cloudinary_url = "/static/img/blog.png"
        else:
            cloudinary_url = "/static/img/blog.png"

        pauthor = writer.firstName
        ptimestamp = formatted_time
        pusername = slug

        Post.objects.create(username=pusername, title=ptitle, postImage=cloudinary_url,content=pcontent, author=pauthor, slug=pslug, timeStamp=ptimestamp)
        
        messages.success(request, 'Your post has been uploaded successfully')

        return redirect(f'/writers/profile/{slug}')

class EditBlogView(View):
    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        context = {'post':post}
        return render(request, 'writers/editBlog.html', context)

    def post(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        ptitle = request.POST.get('title', post.title)
        ppicture = request.FILES.get('picture')

        if ppicture:
            if ppicture.size > 0:
                # Upload the file to Cloudinary
                upload_result = cloudinary.uploader.upload(
                    ppicture,
                    public_id=f"iCoder/media/posts/{slug}",
                    overwrite=True,
                    resource_type="image"
                )

                # save the Cloudinary URL to the user's profile
                cloudinary_url = upload_result['secure_url']
            else:
                cloudinary_url = post.postImage
        else:
            cloudinary_url = post.postImage
            
        pcontent = request.POST.get('content', post.content)
        pslug = request.POST.get('slug', post.slug)
        post.title = ptitle
        post.slug = pslug
        post.content = pcontent
        post.postImage = cloudinary_url
        post.save()

        messages.success(request, 'Your post has been successfully updated.')
        return redirect(f'/writers/profile/{post.username}')

class DeleteBlogView(View):
    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        post.delete()
        messages.success(request, 'Your post has been deleted successfully')
        return redirect(f'/writers/profile/{request.user.username}')



    
    


