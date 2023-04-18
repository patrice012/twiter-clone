import pytest

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import forms
from django.forms.widgets import PasswordInput

from auth_app.forms import RegisterForm

@pytest.fixture
def form_data():
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword123',
    }

@pytest.fixture
def existing_user():
    user = get_user_model().objects.create_user(
        username='existinguser',
        email='existinguser@example.com',
        password='existingpassword123',
    )
    return user

class TestRegisterForm:

    @pytest.mark.django_db
    def test_form_valid(self, form_data):
        form = RegisterForm(data=form_data)
        assert form.is_valid()
        assert form.cleaned_data['username'] == 'testuser'
        assert form.cleaned_data['email'] == 'testuser@example.com'
        assert form.cleaned_data['password'] == 'testpassword123'

    @pytest.mark.django_db
    def test_form_invalid_email(self, form_data, existing_user):
        # Test for invalid email
        form_data['email'] = 'existinguser@example.com'
        form = RegisterForm(data=form_data)
        assert not form.is_valid()
        assert 'email' in form.errors
        assert form.errors['email'][0] == 'This email already exist...'

    def test_password_widget(self, form_data):
        # Test that password field has PasswordInput widget
        form = RegisterForm()
        assert isinstance(form.fields['password'].widget, PasswordInput)
