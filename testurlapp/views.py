from django.shortcuts import render


# Create your views here.


def home_month(request, month):
    return render(request, 'home.html', {})


def home_year(request, month, year):
    return render(request, 'home.html', {})