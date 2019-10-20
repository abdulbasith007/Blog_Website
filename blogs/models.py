from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=200)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        #return reverse('blog-home')
        return reverse('post-details',kwargs={'pk':self.pk})