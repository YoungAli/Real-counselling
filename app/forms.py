from django import forms
from .models import Article, Appointment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Enter the article's title"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Start typing..."}))
    image_url = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': "Enter the image url"}))
    tags = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': "Enter the tags separated with commas"}))
    class Meta:
        model = Article
        fields = ['title', 'tags', 'image_url', 'content']


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        label="Select the date", required=True,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    start_time = forms.TimeField(
        label="Select the start time", required=True,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    end_time = forms.TimeField(
        label="Select the end time", required=True,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )

    class Meta(forms.ModelForm):
        model = Appointment
        fields = ['date', 'start_time', 'end_time']


class ScheduleAppointmentForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Appointment
        fields = ['in_person', 'virtual']

