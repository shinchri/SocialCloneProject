from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from groups.models import Group
# POSTS MODELS
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_models()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now = True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey.(Group, related_name='post', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaa

    def get_absolute_url(self):
        return reverse('post:single', kward={'username':self.user.username, 'pk'=self.pk})                                                                                                                      \\\\\\\\")

    class Meta:
        ordering =['-creted_at']
        unique_together = ['user','message']
