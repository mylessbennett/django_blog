from django.forms import ModelForm
from blog.models import Comment, Article


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'message']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'author']
