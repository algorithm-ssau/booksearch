from django.contrib.auth import get_user_model
from django.conf import settings

class AuthenticationEmailBackend(object):
    """
    Email Authentication Backend

    Allows a user to sign in with either a username or an email address
    """
    def authenticate(self, request, username=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)    
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
