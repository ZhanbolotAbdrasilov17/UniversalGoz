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

class DescSurgery(admin.TabularInline):
    model = SurgeryFullDescription

<<<<<<< HEAD

class SurgeryAdmin(admin.ModelAdmin):
    inlines = [DescSurgery, ]


admin.site.register(Treatment, TreatmentAdmin)

=======
>>>>>>> 65f2247ef83f7c50880a76e780102b722ad065ed
class DescSurgery(admin.TabularInline):
    model = SurgeryFullDescription


class SurgeryAdmin(admin.ModelAdmin):
    inlines = [DescSurgery, ]

admin.site.register(Surgery, SurgeryAdmin)


admin.site.register(FAQ)
admin.site.register(Reviews)