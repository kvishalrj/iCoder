from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Post
from writers.models import Writer

# HTML Pages

def home(request):
    allPosts = Post.objects.all()
    trendPost = [post for post in allPosts]
    trendPost.sort(key=lambda p: p.views, reverse=True)
    trendPost = trendPost[:3]
    context = {'posts' : trendPost}
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the form correctly!')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
    
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)==0:
        messages.warning(request, "Enter your search first!")
        return redirect(request.META['HTTP_REFERER'])
    if len(query)>78:
        allPosts = {}
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostTitle.union(allPostContent)
    
    if len(allPosts)==0:
        messages.warning(request, "No search results found!")
    params = {'allPosts' : allPosts, 'query' : query}
    return render(request, 'home/search.html', params)

# Authentication APIs

def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # input validations
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, 'Username must be contains alphanumeric characters')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Password must be match')
            return redirect('home')

        # Creating user by built in User model
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        mywriter = Writer(username=username, firstName=fname, lastName=lname, email=email, password=pass2)
        mywriter.save()
        messages.success(request, 'Your account has been successfully created.')
        return redirect('home')
    else:
        return HttpResponse('404 - Error')
    
def handleLogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, Please try again...')
            return redirect('home')
    else:
        return HttpResponse('404 - Error')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('home')
    
