from django.forms import ModelForm
from .models import User, Passenger, Driver


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "enable_loc",
            "frequently_visited",
        ]

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = [
            "pas_user",
        ]

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = [
            "fullname",
        ]