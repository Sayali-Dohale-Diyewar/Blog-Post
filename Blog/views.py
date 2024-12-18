from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Posts, Comment, Reply, CustomUser
from .forms import CommentForm, PostsForm, ReplyForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


from django.contrib.auth import get_user_model

User=get_user_model

@login_required
def Blogpost(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostsForm()  # Reset form after saving
    else:
        form = PostsForm()
    
    blogs = Posts.objects.all()  # Fetch all blog posts
    username = request.user.username
    return render(request, "card.html", {'form': form, 'blogs': blogs, 'username':username})

def CommentBlogPost(request, id):
    
    if request.method == "POST":
        info = CommentForm(request.POST)
        if info.is_valid():
            info.save()
            info=CommentForm()  # Redirect to avoid duplicate form submissions
            return redirect("Blog")
            
    else:
        info = CommentForm()
    
    comments = Comment.objects.all()
    print(comments,"---------------------------------")
    return render(request, "card.html", {'info': info, 'comments': comments})

def ReplyBlogPost(request, comment_id):
    
    if request.method == "POST":
        replyc = ReplyForm(request.POST)
        if replyc.is_valid():
            replyc.save()
            return render(request, "card.html")  # Redirect to avoid duplicate form submissions
    else:
        replyc = ReplyForm()
    
    replyes = Reply.objects.all()
    return render(request, "card.html", {'replyc': replyc, 'replyes': replyes})


def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Debugging statement
            return redirect('Blog')  # Replace 'Blog' with your success page URL name
        else:
            print("Invalid email & password")
    
    return render(request, "login.html")


def Register(request):
    password=make_password('password')
    if request.method == "POST":
        reg = UserForm(request.POST, request.FILES)
        if reg.is_valid():
            user=reg.save()
            user.password = make_password(user.password)  # Hash the password
            user.save()
            reg = UserForm()  # Reset form after saving
        else:
            print(reg.errors)  # Print form errors for debugging
    else:
        reg = UserForm()
    
    regs = CustomUser.objects.all()  # Fetch all Users
    return render(request, "register.html", {'reg': reg, 'regs': regs})

