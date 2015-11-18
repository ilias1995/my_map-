from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from taxi.models import Registr_taxi
from taxi.forms import Taxi_form, TaxiFilter, Registration_user, User_info, Taxi_form_for_users
from django.contrib.auth import login as auth_login

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
            instance = form.save(commit=False)
            instance.name = request.user.first_name
            instance.second_name = request.user.last_name
            instance.save()
            return redirect('/')
    else:
        form = Taxi_form()
    return render(request, 'registeration_taxi.html', {'form': form})

def registration_user(request):
    if request.method == 'POST':
        form = Registration_user(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            auth_login(request, new_user)
            return redirect('/user_info')
    else:
        form = Registration_user
    return render(request, 'registration_user.html', {'form': form})

def user_info(request):
    if request.method == 'POST':
        form = User_info(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = User_info()
    return render(request, 'user_info.html', {'form': form})

def taxi_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'taxi_login.html')

def user_logout(request):
    logout(request)
    return redirect('/')