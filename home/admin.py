from django.contrib import admin
from .models import *


class DescriptionInline(admin.TabularInline):
    model = Description


class DocktorAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline, ]

admin.site.register(Doctor, DocktorAdmin)




class DescNews(admin.TabularInline):
    model = Fulldescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]

admin.site.register(News, NewsAdmin)




class DescTreatment(admin.TabularInline):
    model = TreatmentFullDescription


class TreatmentAdmin(admin.ModelAdmin):
    inlines = [DescTreatment, ]

admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(FAQ)
