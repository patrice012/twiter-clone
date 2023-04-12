from django.db import models

class DateMixins(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)

    class Meta:
        abstract = True