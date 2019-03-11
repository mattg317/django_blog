from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    class Meta:
        permissions = [
            ('can_create_post', 'Can post blog'),
            ('can_update_post', 'Can update blog post'),
            ('can_delete_post', 'Can delete posts'),
        ]
    title = models.CharField(max_length=100)
    #content = models.TextField()
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return full path as string
        return reverse('post-detail', kwargs={'pk' : self.pk})