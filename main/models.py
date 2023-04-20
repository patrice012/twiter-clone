from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField

from core.utils import user_post_diresctory
from main.mixins import DateMixins

from .utils import format_output

User = settings.AUTH_USER_MODEL

# Create your models here.


class Tweet(DateMixins):
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # content = HTMLField()
    tweet_picture = models.ImageField(_("Image"),blank=True, null=True)
    likes_by = models.ManyToManyField(User, related_name='tweet_likes', blank=True, null=True)
    # views_by = models.ManyToManyField(User,related_name='tweet_views',blank=True)
    views_by = models.PositiveIntegerField(_("tweet view by"), default=0, blank=True)

    @property
    def tweet_picture_url(self):
        try:
            url = self.tweet_picture.url
        except:
            url = None
        return url

    @property
    def likes(self):
        return format_output(self.likes_by.count())

    @property
    def view_numbers(self):
        return format_output(self.views_by)
    
    @property
    def users_like_id(self):
        return self.likes_by.values_list('id', flat=True)

    # @property
    # def users_views_id(self):
    #     return self.views_by.values_list('id', flat=True)

