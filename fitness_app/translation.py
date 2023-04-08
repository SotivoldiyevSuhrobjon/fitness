from modeltranslation.translator import register, TranslationOptions
from fitness_app.models import *

@register(Favorite)
class FavoriteTranslation(TranslationOptions):
    fields =('favorite_title','favorite_slug')

@register(FitnessProgramm)
class FavoriteTranslation(TranslationOptions):
    fields =('title','context',)



@register(Article)
class ArticleTranslation(TranslationOptions):
    fields = ('slug','title', 'context')