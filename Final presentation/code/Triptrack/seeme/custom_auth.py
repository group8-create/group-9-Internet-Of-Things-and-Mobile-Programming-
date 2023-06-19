from django.contrib.auth.backends import BaseBackend
from .models import Driver, Passenger

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Driver.objects.get(username=username)
            if user.check_password(password):
                return user
        except Driver.DoesNotExist:
            try:
                user = Passenger.objects.get(username=username)
                if user.check_password(password):
                    return user
            except Passenger.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return Driver.objects.get(pk=user_id)
        except Driver.DoesNotExist:
            try:
                return Passenger.objects.get(pk=user_id)
            except Passenger.DoesNotExist:
                return None
            return None
