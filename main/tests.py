import pytest
import json
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

# Create your tests here.
from main.models import Tweet

User = get_user_model()

# @pytest.fixture
# def tweet_data():
#     user = User.objects.first()
#     _content = "this is just a test"
#     data = {
#         'user':user,
#         'content':_content,
#     }
#     return data


# @pytest.fixture
# def create_tweet(tweet_data):
#     tweet = Tweet.objects.create(**tweet_data)
#     return tweet

# @pytest.mark.django_db
# def test_save_tweet(create_tweet):
#     pass



@pytest.fixture
def user():
    return User.objects.create_user('testuser', 'testuser@example.com', 'testpass')


@pytest.fixture
def tweet_form_data():
    return {
        'content': 'Test tweet content',
        'tweet_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
    }


@pytest.mark.django_db
def test_save_tweet_hxpost(client, user, tweet_form_data):
    client.force_login(user)
    response = client.post(reverse('save_tweet_hxpost'), data=tweet_form_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    assert response.status_code == 200

    content = response.content.decode('utf-8')
    json_data = json.loads(content)
    # tweet_picture = json_data['tweet_picture']


    # print(dir(response), 'this is the reponse')
    # print(json_data, 'context')

    # Check that a Tweet was created with the correct data
    tweet = Tweet.objects.first()
    # print(tweet)
    # assert tweet.content == tweet_form_data['content']
    # assert tweet.tweet_picture.name == tweet_form_data['image'].name

    # Check that the tweet is associated with the correct user
    # assert tweet.user == user

    # # Check that the HTML fragment returned in the response contains the tweet's content
    # assert tweet.content.encode() in response.content