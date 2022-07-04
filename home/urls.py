from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('doctor', doctor, name='doctor'),
    path('doctor/<int:doctors_id>/', DoctorDetail.as_view(), name='doctor'),
    path('news', news, name='news'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('about_2', about_2, name='about_2'),
    path('faq', faq, name='faq'),
    path('treatment', treatment, name='treatment'),
    path('treatment/<int:treatment_id>/', TreatmentDetail.as_view(), name='treatment'),
    path('research_single', research_single, name='research_single'),
    path('surgery', surgery, name='surgery'),
    path('surgery/<int:surgery_id>/', SurgeryDetail.as_view(), name='surgery'),
    path('surgery_single', surgery_single, name='surgery_single'),
    path('service', service, name='service'),
    path('appeal/', appeal, name='appeal'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)