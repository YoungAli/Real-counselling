from __future__ import print_function

import datetime, time, os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings
from django.core.mail import send_mail


# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ['https://www.googleapis.com/auth/calendar']



def add_to_calendar(student_email, start_time, end_time, meet_code=None):
    """
    Used to schedule the counselling seesion, making use of Google Calendar API
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        if meet_code:
            location = f"Virtual - Google Meet Link: https://meet.google.com/{meet_code}"
        else:
            location = "Counsellor's Office",

        events = {
            'summary': 'Counselling Session',
            'location': location,
            'description': 'One-on-One Counselling Session',
            'start': {
                'dateTime': start_time,
                'timeZone': 'Africa/Lagos',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Africa/Lagos',
            },

            'attendees': [ # put counsellor and student's email here
                {'email': "emmanuel.tanimowo@trinityuniversity.edu.ng"},
                {'email': student_email},

            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'popup', 'minutes': 90},
                ],
            }
        }

        event = service.events().insert(calendarId='primary', body=events).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print('An error occurred: %s' % error)


def format_scheduled_date(date_):
    """function used to format the scheduled date"""
    appointment_date = f"{date_.strftime('%A')} {date_.strftime('%B')} {date_.day}, {date_.year}"
    return appointment_date


def format_scheduled_time(start_time, end_time):
    """function used to format the scheduled time"""
    start_time_ = f"{str(start_time).split(':')[0]}:{str(start_time).split(':')[1]}"
    end_time_ = f"{str(end_time).split(':')[0]}:{str(end_time).split(':')[1]}"
    f_start_time_ , f_end_time_ = time.strptime(start_time_, "%H:%M"), time.strptime(end_time_, "%H:%M")
    start_time_value, end_time_value = time.strftime( "%I:%M %p", f_start_time_), time.strftime( "%I:%M %p", f_end_time_)
    return start_time_value, end_time_value


def format_session_interval(appointment_date, start_time, end_time):
    """unction to format the session interval to be used for adding event to google calendar"""
    start_schedule_time = f"{start_time.split(':')[0]}:{start_time.split(':')[1]}:{start_time.split(':')[2]}"
    end_schedule_time = f"{end_time.split(':')[0]}:{end_time.split(':')[1]}:{end_time.split(':')[2]}"
    start_scheduled_datetime, end_scheduled_datetime = f"{appointment_date}T{start_schedule_time}", f"{appointment_date}T{end_schedule_time}"
    return start_scheduled_datetime, end_scheduled_datetime


def send_mail_to_counsellor(first_name, last_name, appointment_type, scheduled_date, start_time , end_time, meet_code=None):
    """function to send email to counsellor informing about the scheduled session"""
    if meet_code:
        message_ = f"A counselling session has been scheduled by {first_name} {last_name}. \n\nType: {appointment_type} \n\nDate: {scheduled_date} \n\nTime: {start_time} - {end_time} \n\n\nKindly use this link to join the session:\n\nhttps://meet.google.com/{meet_code} \n\n\n\nRegards, \n\n\nTU-Counsel Team"
    else:
        message_ = f"A counselling session has been scheduled by {first_name} {last_name}. \n\nType: {appointment_type} \n\nDate: {scheduled_date} \n\nTime: {start_time} - {end_time} \n\n\n\nRegards, \n\n\nTU-Counsel Team"
    subject = 'Counselling Session Alert'
    message = message_
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['emmanuel.tanimowo@trinityuniversity.edu.ng',]  # counsellor email here
    send_mail(subject, message, email_from, recipient_list)


def send_mail_to_student(first_name, last_name, appointment_type, scheduled_date, start_time , end_time, student_email, meet_code=None):
    """function to send email to student informing them about the scheduled session"""
    if meet_code:
        message_ = f"Hello {first_name} {last_name}, \n\nYour counselling session has been successfully scheduled. \n\n\nType: {appointment_type} \n\nDate: {scheduled_date} \n\nTime: {start_time} - {end_time} \n\n\nKindly use this link to join the session:\n\nhttps://meet.google.com/{meet_code}   \n\n\n\nRegards, \n\n\nTU-Counsel Team"
    else:
        message_ = f"Hello {first_name} {last_name}, \n\nYour counselling session has been successfully scheduled. \n\n\nType: {appointment_type} \n\nDate: {scheduled_date} \n\nTime: {start_time} - {end_time} \n\n\n\nRegards, \n\n\nTU-Counsel Team"
    subject = 'Counselling Session Confirmation'
    message = message_
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [student_email]  # student email here
    send_mail(subject, message, email_from, recipient_list)

