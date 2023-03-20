import pytest
import uuid

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, reverse, get_object_or_404


from profil.models import Profile, SocialLink


