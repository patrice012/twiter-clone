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
    tweet_picture = models.ImageField(_("Image"), upload_to=user_post_diresctory, height_field=None, width_field=None, max_length=None, blank=True, null=True)

