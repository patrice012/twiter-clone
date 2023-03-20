from django.apps import AppConfig
from django.core.signals import request_finished
from django.contrib.auth.signals import user_login_failed
from django.contrib.auth import get_user_model



class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_app'

    def ready(self):
        from .signals import create_profile


