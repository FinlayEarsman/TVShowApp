from django.contrib import admin
from TVShowApp.models import Genre, Show, Belonging, Review


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name',)


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Show)
admin.site.register(Belonging)
admin.site.register(Review)