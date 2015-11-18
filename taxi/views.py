from django.shortcuts import render, redirect
from taxi.models import Registr_taxi
from taxi.forms import Taxi_form, TaxiFilter

def index(request):
    registr_taxi = Registr_taxi.objects.all()
    f = TaxiFilter(request.GET, queryset=Registr_taxi.objects.all())
    return render(request, 'index.html', {'registr_taxi': registr_taxi, 'filter': f})

def know_more(request, id):
    register_taxi = Registr_taxi.objects.get(pk=id)
    return render(request, 'know_more.html', {'register_taxi': register_taxi})


def contacts(request):
    return render(request, 'contact.html')

def registeration_taxi(request):
    if request.method == 'POST':
        form = Taxi_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Taxi_form()
    return render(request, 'registeration_taxi.html', {'form': form})