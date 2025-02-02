from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

