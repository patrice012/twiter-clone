from django import forms
from tinymce.widgets import TinyMCE

from main.models import Tweet

# from .models import Tweet

class TweetForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Tweet
        fields = ['content', 'tweet_picture']