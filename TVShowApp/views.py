from django.shortcuts import render, redirect, reverse, Http404
from django.http import HttpResponse
from .models import Genre, Show, Belonging, Review
from .forms import GenreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required
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


# all operations for genres

@login_required
def add_genres(request):
    # # if user is login and admin
    if request.user.id == 1:
        # A HTTP POST?
        if request.method == "POST":
            form = GenreForm(request.POST)
            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                form.save(commit=True)
                # Now that the category is saved, we could confirm this.
                # For now, just redirect the user back to the index view.
                return HttpResponse("ok")
            else:
                # The supplied form contained errors -
                err = form.errors
                return HttpResponse(err)

        else: # GET METHOD
            form = GenreForm()
            return HttpResponse(form)
    else:
        return redirect(reverse("TVShowApp:login"))


@login_required
def delete_genres(request, id):
    try:
        p = Genre.objects.get(id=id)
        p.delete()
    except p.DoesNotExist:
        raise Http404("Poll does not exist")
    return HttpResponse("ok")