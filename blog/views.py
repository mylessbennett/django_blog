from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from blog.forms import CommentForm, ArticleForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def blog_post(request, id):
    article = get_object_or_404(Article, pk=id)
    form = CommentForm(request.POST)
    context = {'article': article, 'form': form}
    response = render(request, 'blog_post.html', context)
    return HttpResponse(response)


def create_comment(request):
    blog_post = Article.objects.get(pk=request.POST['blog_post_id'])
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.instance
        comment.blog_post = blog_post
        comment.save()
        return HttpResponseRedirect('/post/' + request.POST['blog_post_id'])
    else:
        return render(request, 'blog_post.html', {'form': form})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        form = UserCreationForm()
    http_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(http_response)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            form.add_error('username', 'Login Failed')
    else:
        form = LoginForm()
    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
