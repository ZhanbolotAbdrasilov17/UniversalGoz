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
    path('faq', faq, name='faq'),
    path('treatment', treatment, name='treatment'),
    path('treatment/<int:treatment_id>/', TreatmentDetail.as_view(), name='treatment'),
    path('surgery', surgery, name='surgery'),
    path('surgery/<int:surgery_id>/', SurgeryDetail.as_view(), name='surgery'),
    path('service', service, name='service'),
    path('appeal/', appeal, name='appeal'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)