from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post_name', 'post_value',)
