from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self,request, username=None, password=None):
        """
            this method is used to authenticate the current user.
            Check if the user is in the backends defined in AUTHENTICATION_
            BACKENDS one by one, until one of them successfully authenticates the user
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        """
            django will use this method to get the current user base on their pk
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None