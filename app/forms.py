from django import forms
from .models import Article, Appointment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter the article's title"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Start typing..."}))
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'tags', 'content']


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        label="Select the date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    start_time = forms.TimeField(
        label="Select the start time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    end_time = forms.TimeField(
        label="Select the end time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )

    class Meta(forms.ModelForm):
        model = Appointment
        fields = ['date', 'start_time', 'end_time']


class ScheduleAppointmentForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Appointment
        fields = ['booked']

