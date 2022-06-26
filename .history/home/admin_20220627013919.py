from django.contrib import admin
from .models import *


class DescriptionInline(admin.TabularInline):
    model = Description


class Docktoradmin(admin.Modeladmin):
    inlines = [DescriptionInline, ]

admin.site.register(Doctor, Docktoradmin)


class DescNews(admin.TabularInline):
    model = Fulldescription


class Newsadmin(admin.Modeladmin):
    inlines = [DescNews, ]

admin.site.register(News, Newsadmin)
