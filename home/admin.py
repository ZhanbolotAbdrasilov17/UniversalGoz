from django.contrib import admin
from .models import *


class DescriptionInline(admin.TabularInline):
    model = Description


class DocktorAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline, ]

admin.site.register(Doctor, DocktorAdmin)

