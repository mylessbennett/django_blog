from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from blog.models import Comment, Article
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'message']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }

        def validate_published_date(self):
            present_date = datetime.today()
            draft = self.cleaned_data['draft']
            if draft is True:
                if self.published_date < present_date:
                    raise ValidationError('If this is a draft, date must be in the future.')
            else:
                if self.published_date > present_date:
                    raise ValidationError('If this is not a draft, date must be in the past.')
