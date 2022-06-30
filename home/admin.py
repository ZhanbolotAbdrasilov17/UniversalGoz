from django.contrib import admin
from .models import *


class DescriptionInline(admin.TabularInline):
    model = Description


class DocktorAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline, ]

admin.site.register(Doctor, DocktorAdmin)



<<<<<<< HEAD

=======
>>>>>>> edd88213fccf6084ad3678df96b7d4c8e0477a8d
class DescNews(admin.TabularInline):
    model = Fulldescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]

admin.site.register(News, NewsAdmin)

<<<<<<< HEAD



class DescTreatment(admin.TabularInline):
    model = TreatmentFullDescription


class TreatmentAdmin(admin.ModelAdmin):
    inlines = [DescTreatment, ]

admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(FAQ)
=======
class DescHeadlines(admin.TabularInline):
    model = DescriptionHeadlines

class HeadlinesAdmin(admin.ModelAdmin):
    inlines = [ DescHeadlines, ]

admin.site.register(Headlines, HeadlinesAdmin)


>>>>>>> edd88213fccf6084ad3678df96b7d4c8e0477a8d
