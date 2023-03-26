from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

from core.utils import user_diresctory


User = settings.AUTH_USER_MODEL

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True,max_length=254)
    profile_name = models.CharField(_("Profile name"),blank=True, null=True, max_length=50)
    profile_picture = models.ImageField(_("Picture"), upload_to=user_diresctory, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover_picture = models.ImageField(_("Cover picture"), upload_to=user_diresctory, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    # bio = models.TextField(_("Say more about you."), null=True, blank=True)
    about = HTMLField()
    location=models.CharField(_("Your current location"), max_length=50)
    career = models.CharField(_("Your career"), max_length=50)


    def __str__(self):
        # return '{0} for {1}'.format(self.profile_name, str(self.user.username))
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    
    @property
    def num_of_social_links(self):
        return self.social_links.all().count()

    @property
    def cover_picture_url(self):
        try:
            url = self.cover_picture.url
        except:
            url = None
        return url

    @property
    def profile_picture_url(self):
        try:
            url = self.profile_picture.url
        except:
            url = None
        return url


class SocialLink(models.Model):
    for_profile = models.ForeignKey(Profile, related_name= 'social_links', on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField(_("You're social link"),null=True, blank=True, max_length=200)
    link_name = models.CharField(_("Social app name"), max_length=50)


    def __str__(self):
        return f'{self.link} for {self.for_profile}'
    


class Contact(models.Model):
    user_from = models.ForeignKey(User,related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'
    

user_model = get_user_model()

field_expr=models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)


#because we don't have access to the User models directly we need to use add_to_class()
user_model.add_to_class('following', field_expr)