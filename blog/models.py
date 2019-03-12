from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateTimeField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
