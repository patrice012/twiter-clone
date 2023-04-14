from django.contrib.auth import get_user_model
from django.test import RequestFactory
from myapp.backends import EmailAuthBackend

class TestEmailAuthBackend:
    def setup_method(self, method):
        self.backend = EmailAuthBackend()
        self.request_factory = RequestFactory()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_authenticate_valid_credentials(self):
        request = self.request_factory.post('/login/', {'email': self.user_data['email'], 'password': self.user_data['password']})
        user = self.backend.authenticate(request=request, username=self.user_data['email'], password=self.user_data['password'])
        assert user == self.user

    def test_authenticate_invalid_credentials(self):
        request = self.request_factory.post('/login/', {'email': self.user_data['email'], 'password': 'wrongpassword'})
        user = self.backend.authenticate(request=request, username=self.user_data['email'], password='wrongpassword')
        assert user is None

    def test_get_user(self):
        user_id = self.user.pk
        user = self.backend.get_user(user_id)
        assert user == self.user

    def test_get_user_invalid_id(self):
        user = self.backend.get_user(123456)
        assert user is None
