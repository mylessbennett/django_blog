from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
