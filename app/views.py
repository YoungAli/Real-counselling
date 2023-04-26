from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Article, Counsel
from .forms import ArticleForm, CounselForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .decorators import for_admins
from googleapiclient.discovery import build
from decouple import config


class HomePageView(TemplateView):
    template_name = 'home.html'
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


@login_required(login_url='login')
def all_videos(request):
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context = {}
        youtube = build('youtube', 'v3', developerKey=config('YOUTUBE_API_KEY'))
        request = youtube.search().list(q=f'{search_input}', part='snippet', type='video', maxResults=50)
        response = request.execute()
        for i in res['items']:
            video_id, video_title = i['id']['videoId'], i['snippet']['title']
            video_description, video_thumbnail = i['snippet']['description'], i['snippet']['thumbnails']['default']
            context[video_id] = {'title': video_title, 'description': video_description, 'thumbnail': video_thumbnail}

    return render(request, 'videos.html', context)

@login_required(login_url='login')
def all_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context)


@login_required(login_url='login')
@for_admins
def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'create_article.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else: return render(request, 'create_article.html', {'form': form})


@login_required(login_url='login')
@for_admins
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_title = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    return render(request, 'edit_article.html', {'form': form, 'slug': slug, 'article_title': article_title})

@login_required(login_url='login')
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_title = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    context = {'form':form, 'slug':slug, 'article_title':article_title}
    return render(request, 'article_detail.html', context)

@login_required(login_url='login')
@for_admins
def delete_article(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return redirect('articles')


# def page_not_found(request, exception):
#     return render(request, '404.html')


# def server_error_page(request, exception):
#     return render(request, '500.html')
