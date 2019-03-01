from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    context = {'date': datetime.now().strftime('%A %B %d %Y')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
