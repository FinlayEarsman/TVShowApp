from django.shortcuts import render, redirect, reverse, Http404
from .models import Genre

def add_variable_to_context(request):
    genres = Genre.objects.all()
    return {
        'genres': genres
    }