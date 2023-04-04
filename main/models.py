from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField

from core.utils import user_post_diresctory
from .mixins import DateMixins

User = settings.AUTH_USER_MODEL

# Create your models here.


class Tweet(DateMixins):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # content = HTMLField()
    tweet_picture = models.ImageField(_("Image"),blank=True, null=True)
    likes_by = models.ManyToManyField(User, related_name='tweet_likes', blank=True)
    views_by = models.ManyToManyField(User,related_name='tweet_views',blank=True)


    @property
    def tweet_picture_url(self):
        try:
            url = self.tweet_picture.url
        except:
            url = None
        return url

    @property
    def likes(self):
        return self.likes_by.count()

    @property
    def view_numbers(self):
        return self.views_by.count()
    
    @property
    def users_like_id(self):
        return self.likes_by.values_list('id', flat=True)

