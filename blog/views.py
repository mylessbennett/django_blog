from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Comment


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def blog_post(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {'article': article}
    response = render(request, 'blog_post.html', context)
    return HttpResponse(response)


def create_comment(request):
    Comment.objects.create(
        user_name=request.POST['user_name'],
        message=request.POST['message'],
        blog_post=Article.objects.get(pk=request.POST['blog_id'])
    )
    return HttpResponseRedirect('/post/' + request.POST['blog_id'])
