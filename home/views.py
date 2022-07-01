from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.conf import settings


from .models import *


def appeal(request):
    if request.method == 'POST':
        data = request.POST
        msg = f'Тема {data["subject"]} \n ФИО {data["name"]}\n' \
              f' Текст {data["message"]} \n Email {data["email"]}' \
              f'Телефон {data["phone"]}'
        send_mail('Образец', msg, settings.EMAIL_HOST_USER, ['zhanbolot19971997@gmail.com'])
    return HttpResponseRedirect(redirect_to=reverse('contact'))


def home(request):
    doctors = Doctor.objects.all()
    news = News.objects.all()
    reviews = Reviews.objects.all()
    context = {"doctors": doctors, "news": news, "reviews": reviews}
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

class TreatmentDetail(DetailView):
    model = Treatment
    template_name = "research_single.html"
    context_object_name = 'treatment'
    pk_url_kwarg = 'treatment_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['treatment_desc'] = TreatmentFullDescription.objects.all()
        return context


def contact(request):
    context = {"token": get_token(request)}
    return render(request, 'contact.html', context)


def about(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors, }
    return render(request, 'about.html', context)

def about_2(request):
    return render(request, 'about_2.html')

def faq(request):
    faqs = FAQ.objects.all()
    context = {"faqs": faqs}
    return render(request, 'faq.html', context)

def treatment(request):
    treatments = Treatment.objects.all()
    context = {"treatments": treatments}
    return render(request, 'research.html', context)

def research_single(request):
    return render(request, 'research_single.html')

def service(request):
    return render(request, 'service.html')



