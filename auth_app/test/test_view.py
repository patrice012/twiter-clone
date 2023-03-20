import pytest
import uuid

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, reverse, get_object_or_404


User = get_user_model()


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
def test_signin_view(client):
    url = reverse('register')
    data = {'username':'dave','email':'dave@gmail.com','password':'dave0123'}
    response = client.post(url, data)
    assert response.status_code == 302



@pytest.mark.django_db
def test_login_action_with_email_address(client,create_user):
    user = create_user(username='dave',email='dave@gmail.com',password='dave0123')
    url = reverse('login')
    data = {'username':'dave@gmail.com','password':'dave0123'}
    response = client.post(url, data)
    assert response.status_code == 200






# @pytest.mark.django_db
# def test_super_user_view(admin_client):
#     url = reverse('superuser-url')
#     response = admin_client.get(url)
#     assert response.status_code == 200



# @pytest.mark.django_db
# def test_unauthorized(client):
#     url = reverse('superuser-url')
#     response = client.get(url)
#     assert response.status_code == 401






