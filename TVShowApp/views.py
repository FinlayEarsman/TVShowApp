from django.shortcuts import render, redirect, reverse, Http404
from django.http import HttpResponse
from .models import Genre, Show, Belonging, Review
from .forms import GenreForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


#@login_required
def index(request):
    show_list = Show.objects.order_by('-avg_rating')[:5]
    context_dict = {}
    context_dict['shows'] = show_list
    return render(request, 'TVShowApp/index.html', context=context_dict)


def tv_show(request):
    #needs the slug/name of the show to be passed to template
    return render(request, 'TVShowApp/tv_show.html')


def genres(request):
    return render(request, 'TVShowApp/genre.html')


def new_rating(request):
    #this isn't currently working because there isnt any shows
    return render(request, 'TVShowApp/add_rating.html')


def request_show(request):
    return render(request, 'TVShowApp/request_show.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse("TVShowApp:index"))
        else:
            # Return an 'invalid login' error message.
            messages.add_message(request, messages.INFO, 'invalid login, please check your inputs!')

    return render(request, 'TVShowApp/login.html')


def user_profile(request):
    return render(request, 'TVShowApp/user_profile.html')


def sign_up(request):
    return render(request, 'TVShowApp/sign_up.html')


def search_results(request):
    return render(request, 'TVShowApp/search_results.html')


def review_requests(request):
    return HttpResponse("admin show request approval page")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('TVShowApp:index'))


# all operations for genres

@login_required
def add_genres(request):
    # # if user is login and admin
    if request.user.is_superuser:
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
        return redirect(reverse("TVShowApp:index"))


@login_required
def delete_genres(request, id):
    try:
        p = Genre.objects.get(id=id)
        p.delete()
    except p.DoesNotExist:
        raise Http404("Poll does not exist")
    return HttpResponse("ok")
