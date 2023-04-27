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
import random


class HomePageView(TemplateView):
    template_name = 'home.html'
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


@login_required(login_url='login')
def all_videos(request):
    search_input = request.GET.get('search-area')
    youtube = build('youtube', 'v3', developerKey=config('YOUTUBE_API_KEY'))
    print('search...', search_input)
    if search_input == None:
        keywords = ['anxiety', 'relationship', 'career', 'addiction','education', 'anger', 'mental health', 'spiritual']
        search_input = random.choice(keywords)
        req = youtube.search().list(q=f'{search_input} counselling', part='snippet', type='video', maxResults=50)
        res= req.execute()
    else:
        req = youtube.search().list(q=f'{search_input}', part='snippet', type='video', maxResults=50)
        res = req.execute()
    videos = []
    for i in res['items']:
        video_id = i['id']['videoId']
        video_title = i['snippet']['title']
        video_description = i['snippet']['description']
        video_thumbnail = i['snippet']['thumbnails']['default']
        videos.append({'id': video_id, 'title': video_title, 'description': video_description, 'thumbnail': video_thumbnail})
    context = {'videos': videos}
    return render(request, 'videos.html', context)

@login_required(login_url='login')
def all_articles(request):
    search_input = request.GET.get('search-area')
    print('search......',search_input)
    if search_input == None:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(title__contains=search_input)
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
