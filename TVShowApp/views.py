from django.shortcuts import render, redirect, reverse, Http404
from django.http import HttpResponse
from .models import Genre, Show, Belonging, Review
from .forms import GenreForm, UserForm, ReviewForm, ShowForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View


def index(request):
    context_dict = {}
    genre_list = Genre.objects.all()
    show_list = Show.objects.filter(reviewed=True).order_by('-avg_rating')[:5]
    context_dict['shows'] = show_list
    context_dict['genres'] = genre_list
    return render(request, 'TVShowApp/index.html', context=context_dict)


def tv_show(request, show_id):
    context_dict = {}
    try:
        show = Show.objects.get(id=show_id)
        reviews = Review.objects.filter(show=show.id)
        belongings = Belonging.objects.filter(show=show)
        genres = []
        for belonging in belongings:
            genres.append(Genre.objects.get(name=belonging.genre))
        context_dict['show'] = show
        context_dict['reviews'] = reviews
        context_dict['show_genres'] = genres
    except Show.DoesNotExist:
        context_dict['show'] = ""
        
    return render(request, 'TVShowApp/tv_show.html', context=context_dict)


def show_genre(request, genre_name_slug):
    context_dict = {}
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        belongings = Belonging.objects.filter(genre=genre)
        shows_in_genre = []
        for belonging in belongings:
            s = Show.objects.get(id=belonging.show.id)
            if s.reviewed:
                shows_in_genre.append(s)
        context_dict['genre'] = genre
        context_dict['shows'] = shows_in_genre
    except Genre.DoesNotExist:
        context_dict['genre'] = ""
        context_dict['shows'] = ""
    return render(request, 'TVShowApp/genre.html', context=context_dict)


def new_rating(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(show=show, comment=form.cleaned_data['comment'], rating=form.cleaned_data['rating'],
                            user=request.user)
            review.save()

            reviews_for_show = Review.objects.filter(show=show)
            total = 0
            for rev in reviews_for_show:
                total += rev.rating
            average_across_reviews = total / len(reviews_for_show)
            show.avg_rating = round(average_across_reviews, 1)
            show.save()
            return redirect(reverse("TVShowApp:index"))
        else:
            print(form.errors)
    else:
        form = ReviewForm()
        context_dict = {'show': show, 'form': form}
        return render(request, 'TVShowApp/add_rating.html', context=context_dict)


def request_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid:
            s = Show.objects.create(title=request.POST['show_name'], year=request.POST['year_released'], avg_rating=0,
                                    photo=request.FILES.get('photo'), reviewed=False)
            s.save()

            for genre in Genre.objects.all():
                if genre.slug in request.POST.keys():
                    Belonging.objects.get_or_create(genre=genre, show=s)[0]

            return redirect(reverse("TVShowApp:index"))
        else:
            print(form.errors)
    else:
        form = ReviewForm()
        genres = Genre.objects.all()
        context_dict = {'form': form,
                        'genres': genres}
        return render(request, 'TVShowApp/request_show.html', context=context_dict)


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
            messages.add_message(request, messages.INFO, 'Invalid login, please check your inputs!')

    return render(request, 'TVShowApp/login.html')


def user_profile(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        reviews = Review.objects.filter(user=user)
        context_dict['reviews'] = reviews
        context_dict['usr_prof'] = user
    except User.DoesNotExist:
        context_dict['reviews'] = ""
        context_dict['reviews'] = ""
    return render(request, 'TVShowApp/user_profile.html', context=context_dict)


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'TVShowApp/sign_up.html', context={'user_form': user_form, 'registered': registered})


def search_results(request):
    if request.method == "POST":
        context_dict = {}
        search_result = request.POST['search_bar']
        users = User.objects.filter(username__contains=search_result)
        shows = Show.objects.filter(title__contains=search_result).filter(reviewed=True)
        context_dict['search_result'] = search_result
        context_dict['shows'] = shows
        context_dict['users'] = users
        return render(request, 'TVShowApp/search_results.html', context=context_dict)
    else:
        return render(request, 'TVShowApp/search_results.html')


def review_requests(request):
    context_dict = {}
    show_genres = {}
    unreviewed_shows = Show.objects.filter(reviewed=False)
    for show in unreviewed_shows:
        belongings = Belonging.objects.filter(show=show)
        genres = []
        for belonging in belongings:
            genres.append(Genre.objects.get(name=belonging.genre))
        show_genres[show] = genres
    context_dict['shows'] = unreviewed_shows
    context_dict['show_genres'] = show_genres
    return render(request, 'TVShowApp/requests.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('TVShowApp:index'))


@login_required
def add_genres(request):
    # if user is login and admin
    if request.user.is_superuser:
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

        else:  # GET METHOD
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
        raise Http404("Genre does not exist")
    return HttpResponse("ok")


class LikeShowView(View):
    @method_decorator(login_required)
    def get(self, request):
        show_id = request.GET['show_id']
        try:
            show = Show.objects.get(id=int(show_id))
        except Show.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        show.likes = show.likes + 1
        show.save()
        return HttpResponse(show.likes)


class ApproveShowRequestView(View):
    @method_decorator(login_required)
    def get(self, request):
        show_id = request.GET['show_id']
        try:
            show = Show.objects.get(id=int(show_id))
        except Show.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        show.reviewed = True
        show.save()
        return HttpResponse(1)


class DenyShowRequestView(View):
    @method_decorator(login_required)
    def get(self, request):
        show_id = request.GET['show_id']
        try:
            show = Show.objects.get(id=int(show_id))
        except Show.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        show.delete()
        return HttpResponse(1)
