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
    path('contact_lenses', contact_lenses, name='contact_lenses'),
    path('comprehensive', comprehensive, name='comprehensive'),
    path('keratoconus', keratoconus, name='keratoconus'),
    path('phakic_lens', phakic_lens, name='phakic_lens'),
    path('retina_diseasea', retina_disease, name='retina_disease'),
    path('glaucoma', glaucoma, name='glaucoma'),
    path('research', research, name='research'),
    path('research_single', research_single, name='research_single'),
    path('service', service, name='service'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)