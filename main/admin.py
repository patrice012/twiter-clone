from django.contrib import admin

# Register your models here.
from main.models import Tweet


@admin.register(Tweet)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user','content', 'tweet_picture_url')