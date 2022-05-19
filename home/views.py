from django.shortcuts import render
from django.views.generic import DetailView

from .models import *


def home(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "home.html", context)


def doctor(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "doctor.html", context)

def news(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "news.html", context)

class NewsDetail(DetailView):
    model = News
    template_name = "news-detail.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

