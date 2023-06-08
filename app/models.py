from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
import string, random

def random_slug():
    return ''.join(random.choice(string.digits) for i in range(12))

class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=50000, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique= True, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def  __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + random_slug())
        super(Article, self).save(*args, **kwargs)


class Appointment(models.Model):
    booked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    in_person = models.BooleanField(default=False)
    virtual = models.BooleanField(default=False)
    type = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique= True, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('appointments')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug())
        super(Appointment, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.date