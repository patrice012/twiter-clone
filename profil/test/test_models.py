import pytest
import uuid

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, reverse, get_object_or_404


from profil.models import Profile, SocialLink

@pytest.fixture
def test_password():
    return 'strong-test-pwd'


@pytest.fixture
def create_user(db,django_user_model,test_password):
    def make_user(**kwargs):
        kwargs['password']=test_password
        if 'username' not in kwargs:
            kwargs['username']=str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def create_relate_profil(db, django_user_model):
    def create_profil(**kwargs):
        name = kwargs.pop('profil_name')
        user = django_user_model.objects.create_user(**kwargs)
        user_profil = Profile.objects.get(user=user)
        user_profil.profil_name=name
        user_profil.save()
        links = ['www.instagram.com','www.twitter.com','www.github.com']
        links_name = ['instagram','twitter','github']

        for i,n in zip(links,links_name):
            social_link=SocialLink.objects.create(for_profile=user_profil, link= i , link_name=n)
        
        return user_profil,user
    return create_profil






@pytest.mark.django_db
def test_create_relate_profil(create_user):
    user = create_user(username='dave',email='dave@gmail.com',password='dave0123')
    profils= Profile.objects.all().count()
    assert profils == 1


@pytest.mark.django_db
def test_create_relate_profil_method(create_relate_profil):
    user_profil,user = create_relate_profil(username='dave',email='dave@gmail.com',password='dave0123', profil_name='dave')
    # assert user_profil.__str__() == 'dave for dave'
    assert user_profil.num_of_social_links == 3 


@pytest.mark.django_db
def test_social_link_count(create_relate_profil):
    user_profil,user = create_relate_profil(username='dave',email='dave@gmail.com',password='dave0123', profil_name='dave')
    social_link_forward = SocialLink.objects.filter(for_profile=user_profil)
    social_link_backward = user_profil.social_links.all()
    assert social_link_backward.count() == social_link_forward.count()


# @pytest.mark.django_db
# def test_create_relate_social_link_count(create_relate_profil):
#     user_profil,user = create_relate_profil(username='dave',email='dave@gmail.com',password='dave0123', profil_name='dave')
#     social_link = user_profil.social_links.all()
#     assert social_link.count() == 3




@pytest.mark.django_db
def test_relate_profil_credentials(create_user):
    user = create_user(username='dave',email='dave@gmail.com',password='dave0123')
    user_profil = Profile.objects.get(user=user)
    assert user_profil.email == user.email
    assert user_profil.user == user


# @pytest.mark.django_deb
# def test_profil_picture_url(self):
#     pass