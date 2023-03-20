from django import forms
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


from profil.models import Profile


User = get_user_model()


class ProfileFrom(forms.ModelForm):
    about = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Profile
        fields = ['email','profile_name','profile_picture','cover_picture','location','career','about']