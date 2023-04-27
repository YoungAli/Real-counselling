from django.urls import path
from .views import HomePageView, DashboardView, create_article, all_articles,  article_detail, delete_article, edit_article, all_videos

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('articles', all_articles, name='articles'),
    path('articles/create', create_article, name='create_article'),
    path('articles/view/<slug:slug>', article_detail, name='article_detail'),
    path('articles/edit/<slug:slug>', edit_article, name='edit_article'),
    path('articles/delete/<slug:slug>', delete_article, name='delete_article'),
    path('videos', all_videos, name='videos'),
    # path('request_counsel', RequestCounselView.as_view(), name='request_counsel'),

]

# handler404 = 'app.views.page_not_found'
# handler500 = 'app.views.server_error_page'
