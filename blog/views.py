from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Article


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
    pass
