from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("TVShowApp Homepage")


def tv_show(request):
    return HttpResponse("TV show display page")


def genres(request):
    return HttpResponse("genres page")


def new_rating(request):
    return HttpResponse("add rating to show page")


def request_show(request):
    return HttpResponse("Request TV show display page")


def login(request):
    return HttpResponse("login page")


def user_profile(request):
    return HttpResponse("profile page")


def sign_up(request):
    return HttpResponse("sign up page")


def search_results(request):
    return HttpResponse("search results page")


def review_requests(request):
    return HttpResponse("admin show request approval page")
