from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
import pytest

from profil.models import Profile

User = get_user_model()

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword123',
    }

@pytest.fixture
def user(user_data):
    return get_user_model().objects.create_user(**user_data)

class TestCreateProfileSignal:

    @pytest.mark.django_db
    def test_create_profile_signal(self, user):
        # post_save.send(sender=get_user_model(), instance=user, created=True)
        try:
            profile = Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            profile = None
        profile = Profile.objects.get(user=user)
        print(profile, 'profile')
        assert profile is not None
        assert profile.user == user
        assert profile.email == user.email
        
    # @pytest.mark.django_db
    # def test_create_profile_signal_not_created(self, user):
    #     post_save.send(sender=get_user_model(), instance=user, created=False)
    #     with pytest.raises(ObjectDoesNotExist):
    #         Profile.objects.get(user=user)
