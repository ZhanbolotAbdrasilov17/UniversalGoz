from django.shortcuts import render
from .models import *


def home(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "home.html", context)


def doctor(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "doctor.html", context)
