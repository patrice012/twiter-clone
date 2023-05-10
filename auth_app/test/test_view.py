import pytest
import uuid

from django.test import RequestFactory, SimpleTestCase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, reverse, get_object_or_404

from auth_app.views import sign_in
from auth_app.forms import RegisterForm

User = get_user_model()

from django.contrib.auth.views import LoginView


@pytest.fixture
def test_password():
    return 'strong-test-pwd'


@pytest.fixture
def create_user(db,django_user_model,test_password):
    def make_user(**kwargs):
        kwargs['password']=test_password
        if 'username' not in kwargs:
            kwargs['username']=str(uuid.uuid4())
        user = django_user_model.objects.create_user(**kwargs)
        return user
    return make_user


@pytest.fixture
def auto_login_user(db,client,create_user,test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username,password=test_password)
        return client, user
    return make_auto_login



@pytest.mark.django_db
def test_auth_login(client):
    user = {'username':'dave','email':'dave@gmail.com','password':'dave0123'}
    client.login(username=user['username'],password=user['password'])
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db
def test_user_create(create_user):
    user = create_user(username='dave',email='dave@gmail.com',password='dave0123')
    assert User.objects.count() == 1



@pytest.mark.django_db
def test_login_action_with_email_address(client,create_user):
    user = create_user(username='dave',email='dave@gmail.com',password='dave0123')
    url = reverse('login')
    data = {'username':'dave@gmail.com','password':'dave0123'}
    response = client.post(url, data)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_sign_in(client):
#     # Create a valid form submission
#     data = {
#         'username': 'testuser',
#         'email': 'testuser@example.com',
#         'password': 'testpassword123',
#     }
#     response = client.post(reverse('register'), data)
#     SimpleTestCase().assertRedirects(response, reverse('login'))

#     # Check that a new user was created with the correct username and email
#     user = User.objects.get(username='testuser')
#     assert user.email == 'testuser@example.com'


@pytest.mark.django_db
def test_sign_in():
    # create a request factory
    factory = RequestFactory()

    # create a POST request with valid data
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword123',
    }
    request = factory.post(reverse('register'), data)

    # call the view function
    response = sign_in(request)

    # check the response
    assert response.status_code == 302  # redirect
    assert response.url == reverse('login')  # redirect to the login page

    # check that the user was created
    user = User.objects.get(username=data['username'])
    assert user.email == data['email']



@pytest.mark.django_db
def test_sign_in_with_inavlid_data():
    # create a POST request with invalid data
    factory = RequestFactory()
    data = {
        'username': 'testuser2',
        'email': 'testuser2@example',
        'password': 'testpassword123',
    }
    request = factory.post(reverse('register'), data)

    # call the view function
    response = sign_in(request)

    # check the response
    assert response.status_code == 200  # form submission failed

    # assert 'password' in response.context['form'].errors  # error message is displayed




