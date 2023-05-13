from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Academic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Email(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    to = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default='no subject')
    body = models.TextField(default='')
    email_date = models.DateTimeField(auto_now_add=True)
    academic = models.BooleanField(default=False)
    category = models.CharField(max_length=255, default='Uncategorized')
    image = models.ImageField(upload_to='images/', blank=True)



    def get_absolute_url(self):
        return reverse('home')


