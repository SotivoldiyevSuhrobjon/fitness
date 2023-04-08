from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


admin.site.register(User)
admin.site.register(SiteInfo)


@admin.register(Favorite)
class FavoriteInfo(TranslationAdmin):
    prepopulated_fields = {'favorite_slug': ('favorite_title',)}


@admin.register(FitnessProgramm)
class FitnessProgramAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'intensity', 'gender', 'part_of_body']


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title']

