from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _

from main.mixins import DateMixins

# Create your models here.

User = settings.AUTH_USER_MODEL

class Comment(DateMixins):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    content = models.TextField(_("Your comment"), blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, default=None, null=True, on_delete=models.SET_NULL)
    object_id = models.PositiveIntegerField(default=None, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # class Meta:
    #     ordering = ['-created']


    def __str__(self):
        return self.content[:50]

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
    

    
    