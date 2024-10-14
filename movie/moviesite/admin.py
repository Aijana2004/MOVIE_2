from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MomentsInline(admin.TabularInline):
    model = Moments
    extra = 1


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieLanguagesInline,MomentsInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Janre)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(History)
admin.site.register(FavoriteMovie)

