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

class DescHeadlines(admin.TabularInline):
    inlines = [DescriptionHeadlines]

class HeadlinesAdmin(admin.ModelAdmin):
    inlines = DescHeadlines

admin.site.register(Headlines, HeadlinesAdmin)
