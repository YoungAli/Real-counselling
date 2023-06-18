from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Article, Appointment
from .forms import ArticleForm, AppointmentForm, ScheduleAppointmentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .decorators import for_admins
from googleapiclient.discovery import build
from decouple import config
import random, time, datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .common import add_to_calendar, format_scheduled_date, format_scheduled_time, format_session_interval, send_mail_to_counsellor, send_mail_to_student

class HomePageView(TemplateView):
    template_name = 'home.html'


@login_required(login_url='login')
def dashboard(request):
    if request.method == "GET":
        articles = Appointment.objects.all()
        return render(request, 'dashboard.html')

@login_required(login_url='login')
@login_required(login_url='login')
def all_videos(request):
    if request.method == "GET":
        return render(request, 'videos.html')


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
@for_admins
def delete_article(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return redirect('articles')


@login_required(login_url='login')
def all_appointments(request):
    search_input = request.GET.get('search-area')
    print('search......',search_input)
    if search_input == None:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.filter(title__contains=search_input)
    context = {'appointments': appointments}
    return render(request, 'appointments.html', context)


@login_required(login_url='login')
def booked_appointments(request):
    search_input = request.GET.get('search-area')
    print('search......',search_input)
    if search_input == None:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.filter(title__contains=search_input)
    context = {'appointments': appointments}
    return render(request, 'booked_appointments.html', context)



@login_required(login_url='login')
@for_admins
def create_appointment(request):
    if request.method == 'GET':
        form = AppointmentForm()
        return render(request, 'create_appointment.html', context={'form': form})
    elif request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            print(dir(form), form.data)
            return redirect('appointments')
        else: return render(request, 'create_appointment.html', {'form': form})


@login_required(login_url='login')
def schedule_appointment(request, slug):
    appointment = get_object_or_404(Appointment, slug=slug)
    form = ScheduleAppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = ScheduleAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment.booked_by = request.user
            if request.POST['session_type'] == 'virtual':
                appointment_type = 'Virtual'
            else: appointment_type = 'In-Person'
            first_name, last_name, user_email = request.user.first_name.title(), request.user.last_name.title(), request.user.email
            print(first_name, last_name, user_email)
            # call function to format the scheduled date
            scheduled_date = format_scheduled_date(appointment.date)

            # call function to format the scheduled time
            start_time, end_time = format_scheduled_time(str(appointment.start_time), str(appointment.end_time))

            # call function to format the session interval to be used for adding event to google calendar
            session_start, session_end = format_session_interval(str(appointment.date), str(appointment.start_time), str(appointment.end_time))

            if request.POST['session_type'] == 'in_person':
                # call function to add the counselling session to google calendar
                add_to_calendar(user_email, session_start, session_end)

                # send email to student and counsellor informing them about the scheduled seesion
                send_mail_to_counsellor(first_name, last_name, appointment_type.title(), scheduled_date, start_time , end_time)
                send_mail_to_student(first_name, last_name, appointment_type.title(), scheduled_date, start_time , end_time, user_email)
                print('..in person')
            elif request.POST['session_type'] == 'virtual':
                meet_codes = ['nkj-kiem-sps', 'ayw-iwdo-emm', 'cod-xsed-zzm', 'kmy-xatr-wvy', 'hba-xjgb-cwj', 'ueq-girz-xqh']
                random_code = random.choice(meet_codes)
                # save the meeting link for that appointment
                appointment.meeting_url = f"https://meet.google.com/{random_code}"
                # call function to add the counselling session to google calendar
                add_to_calendar(user_email, session_start, session_end, random_code)

                # send email to student and counsellor informing about the the schdduled seesion
                send_mail_to_counsellor(first_name, last_name, appointment_type.title(), scheduled_date, start_time , end_time, meet_code=random_code)
                send_mail_to_student(first_name, last_name, appointment_type.title(), scheduled_date, start_time , end_time, user_email, meet_code=random_code)
                print('...virtual')

            print('Emails sent successfully!!')
            appointment.save()
            form.save()
            return redirect('appointments')
    return render(request, 'schedule_appointment.html', {'form': form, 'slug': slug})

@login_required(login_url='login')
@for_admins
def edit_appointment(request, slug):
    appointment = get_object_or_404(Appointment, slug=slug)
    appointment_title = Appointment.objects.get(slug=slug)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    return render(request, 'edit_appointment.html', {'form': form, 'slug': slug, 'appointment_title': appointment_title})

@login_required(login_url='login')
@for_admins
def delete_appointment(request, slug):
    appointment = Appointment.objects.get(slug=slug)
    appointment.delete()
    return redirect('appointments')


# def page_not_found(request, exception):
#     return render(request, '404.html')


# def server_error_page(request, exception):
#     return render(request, '500.html')

