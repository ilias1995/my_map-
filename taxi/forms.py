from django import forms
from django.contrib.auth.models import User
from taxi.models import Registr_taxi, Registration
from django_filters import FilterSet, RangeFilter


class Taxi_form(forms.ModelForm):
    class Meta:
        model = Registr_taxi
        fields = ['name', 'second_name', 'phone_number', 'car_model', 'car_photo', 'price', 'from_where', 'end_time', 'where', 'about']


class TaxiFilter(FilterSet):
    price = RangeFilter()
    class Meta:
        model = Registr_taxi
        fields = ['from_where', 'where', 'price']

class Registration_user(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class User_info(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['phone_number', 'car_model', 'car_photo', 'car_number']

class Taxi_form_for_users(forms.ModelForm):
    class Meta:
        model = Registr_taxi
        fields = ['price', 'from_where', 'end_time', 'where', 'about']