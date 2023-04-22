import pytest
import json
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

# Create your tests here.
from main.models import Tweet

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user('testuser', 'testuser@example.com', 'testpass')


@pytest.fixture
def tweet_form_data():
    return {
        'content': 'Test tweet content',
        # 'tweet_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
    }


@pytest.mark.django_db
def test_save_tweet_hxpost(client, user, tweet_form_data):
    client.force_login(user)
    data = tweet_form_data
    data['user'] =  user
    response = client.post(reverse('save_tweet_hxpost'), data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    assert response.status_code == 200
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.request['PATH_INFO'] == '/save-tweet/'

    # Check that a Tweet was created with the correct data
    tweet = Tweet.objects.first()
    assert tweet.content == tweet_form_data['content']
    # assert tweet.tweet_picture.name == tweet_form_data['image'].name

    # Check that the tweet is associated with the correct user
    assert tweet.user == user

    # Check that the HTML fragment returned in the response contains the tweet's content
    assert tweet.content.encode() in response.content



@pytest.mark.django_db
def test_like_hx_views(client, user, tweet_form_data):
    client.force_login(user)
    # create a tweet object
    data = tweet_form_data
    data['user'] =  user
    client.post(reverse('save_tweet_hxpost'), data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    #  test like action
    t_id = Tweet.objects.first().id
    res = client.get(f'http://localhost:8000/actions/like/{t_id}/')
    t = Tweet.objects.first()
    assert t.likes_by.count() == 1
    assert user.id  in t.users_like_id

    # test dislike action
    res = client.get(f'http://localhost:8000/actions/like/{t_id}/')
    t = Tweet.objects.first()
    assert t.likes_by.count() == 0
    assert user.id  not in t.users_like_id
    

