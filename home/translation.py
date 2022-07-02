from modeltranslation.translator import register, TranslationOptions
from .models import *

#
@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = ('position', )


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', )

@register(Fulldescription)
class DescriptionTranslation(TranslationOptions):
    fields = ('text', )


@register(Description)
class DescriptionTranslation(TranslationOptions):
    fields = ('text', )


@register(Treatment)
class TreatmentTranslation(TranslationOptions):
    fields = ('title', )

@register(TreatmentFullDescription)
class TreatmentFullDescriptionTranslation(TranslationOptions):
    fields = ('text', 'title')

@register(Reviews)
class ReviewsTranslation(TranslationOptions):
    fields = ('text', )

@register(FAQ)
class FAQTranslation(TranslationOptions):
    fields = ('question', 'answer')