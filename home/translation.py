from modeltranslation.translator import register, TranslationOptions
from .models import *

#
@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = ('position', )


@register(Treatment)
class TreatmentTranslation(TranslationOptions):
    fields = ('title', )

@register(TreatmentFullDescription)
class TreatmentFullDescriptionTranslation(TranslationOptions):
    fields = ('text', 'title')

@register(Reviews)
class ReviewsTranslation(TranslationOptions):
    fields = ('text', )