from django import forms
from .models import Article, Counsel

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter the article's title"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Start typing..."}))
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'tags', 'content']


class CounselForm(forms.ModelForm):
    class Meta:
        model = Counsel
        fields = '__all__'
