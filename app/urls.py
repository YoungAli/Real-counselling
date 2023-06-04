from django.urls import path
from .views import (
    HomePageView, DashboardView, create_article, all_articles, delete_article, edit_article, all_videos, all_appointments, create_appointment, edit_appointment, delete_appointment
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('articles', all_articles, name='articles'),
    path('articles/create', create_article, name='create_article'),
    path('articles/edit/<slug:slug>', edit_article, name='edit_article'),
    path('articles/delete/<slug:slug>', delete_article, name='delete_article'),
    path('appointments', all_appointments, name='appointments'),
    path('appointment/create', create_appointment, name='create_appointment'),
    path('appointment/edit/<slug:slug>', edit_appointment, name='edit_appointment'),
    # path('appointment/schedule', schedule_appointment, name='schedule_appointment'),
    # path('appointment/re_schedule/<slug:slug>', re_schedule_appointment, name='re_schedule_appointment'),
    path('appointment/delete/<slug:slug>', delete_appointment, name='delete_appointment'),
    path('videos', all_videos, name='videos'),
    # path('request_counsel', RequestCounselView.as_view(), name='request_counsel'),

]

# handler404 = 'app.views.page_not_found'
# handler500 = 'app.views.server_error_page'
