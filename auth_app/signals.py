from django.contrib.auth.signals import user_login_failed
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete

from django.contrib.auth import get_user_model

from django.core.signals import request_finished
from django.dispatch import receiver


from profil.models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender,instance, **kwargs):
    if 'created' in kwargs and kwargs['created']:
        profile = Profile.objects.create(user=instance, email=instance.email)
        

