from django.shortcuts import render
from django.views.generic import DetailView

from .models import *


def home(request):
    doctors = Doctor.objects.all()
    news = News.objects.all()
    context = {"doctors": doctors, "news":news}
    return render(request, "home.html", context)


def doctor(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "doctor.html", context)


class DoctorDetail(DetailView):
    model = Doctor
    template_name = "doctor-detail.html"
    context_object_name = 'doctors'
    pk_url_kwarg = 'doctors_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = Description.objects.all()
        return context


def news(request):
    newses = News.objects.all()
    context = {"news": newses}
    return render(request, "news.html", context)


class NewsDetail(DetailView):
    model = News
    template_name = "news-detail.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = Fulldescription.objects.all()
        return context


def contact(request):
    return render(request, 'contact.html')


def about(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors, }
    return render(request, 'about.html', context)

def about_2(request):
    return render(request, 'about_2.html')

def faq(request):
    return render(request, 'faq.html')

def contact_lenses(request):
    return render(request, 'contact_lenses.html')

def comprehensive(request):
    return render(request, 'comprehensive.html')

def keratoconus(request):
    return render(request, 'keratoconus.html')

def phakic_lens(request):
    return render(request, 'phakic_lens.html')

def retina_disease(request):
    return render(request, 'retina_disease.html')

def glaucoma(request):
    return render(request, 'glaucoma.html')

def research(request):
    return render(request, 'research.html')

def research_single(request):
    return render(request, 'research_single.html')

def service(request):
    return render(request, 'service.html')
