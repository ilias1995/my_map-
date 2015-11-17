from django import forms
from taxi.models import Registr_taxi

class Taxi_form(forms.ModelForm):
    class Meta:
        model = Registr_taxi
        fields = ['name', 'second_name', 'phone_number', 'car_model', 'car_photo', 'price', 'from_where', 'end_time', 'where', 'about']