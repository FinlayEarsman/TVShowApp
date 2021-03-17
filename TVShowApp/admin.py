from django.contrib import admin
from TVShowApp.models import Genre, Show, Belonging, Review

# Register your models here.
admin.site.register(Genre)
admin.site.register(Show)
admin.site.register(Belonging)
admin.site.register(Review)