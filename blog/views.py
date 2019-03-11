from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Comment
from blog.forms import CommentForm


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
    pass
