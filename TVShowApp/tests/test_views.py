from django.test import TestCase
from TVShowApp.models import Genre, Show, Belonging, Review
from django.http import HttpRequest
from django.urls import reverse
from populate_tv import populate

class IndexViewTests(TestCase):
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('TVShowApp:index'))
        self.content = self.response.content.decode()
        
    def test_index_status_code(self):        
        self.assertEquals(self.response.status_code, 200)

    # is index's URL mapping correct
    def test_index_mapping_exists(self):
        self.assertEquals(reverse('TVShowApp:index'), '/TVShowApp/')

    # does index use correct template    
    def test_index_view_uses_correct_template(self):        
        self.assertTemplateUsed(self.response, 'TVShowApp/index.html')

    # does context dictionary contain all the genres and the specified shows
    def test_index_view_context_dict(self):
        show_list = list(Show.objects.filter(reviewed=True).order_by('-avg_rating')[:5])
        genre_list = list(Genre.objects.all())
        response_show_list = list(self.response.context['shows']);
        response_genre_list = list(self.response.context['genres']);
        
        self.assertEquals(show_list,response_show_list)
        self.assertEquals(genre_list,response_genre_list)

class GenreViewTests(TestCase):
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('TVShowApp:show_genre',kwargs={'genre_name_slug': 'crime'}))
        self.content = self.response.content.decode()
        
    # is it using the correct template
    def test_genre_template(self):
        self.assertTemplateUsed(self.response, 'TVShowApp/genre.html', f"The genre.html template isn't used")

    # does the genre's slug work and is it linked correctly with its name
    def test_genre_slug_functionality(self):
        genre = Genre.objects.get_or_create(name='Crime')[0]
        genre.name = "Different Genre"
        genre.save()
        self.assertEquals('different-genre', genre.slug, f"Changing name of genre doesn't change slug")

    # does context dictionary match up with expected information
    # are the shows being filtered correctly (ie by genre)
    def test_genre_view_context_dict(self):        
        show_list = list(self.response.context['shows'])        

        genre = Genre.objects.get_or_create(name='Crime')[0]
        belongings = Belonging.objects.filter(genre=genre)
        shows_in_genre = []
        for belonging in belongings:
            s = Show.objects.get(id=belonging.show.id)
            if s.reviewed:
                shows_in_genre.append(s)

        self.assertEquals(show_list,shows_in_genre)
        self.assertEquals(self.response.context['genre'],genre)

class BadGenreViewTests(TestCase):            
    def test_nonexistent_genre(self):
        # tries to look up a genre that isnt in the database and checks response
        response = self.client.get(reverse('TVShowApp:show_genre',kwargs={'genre_name_slug':'nonexistent-genre'}))
        lookupString = 'There are no shows in this genre.'
        self.assertIn(lookupString, response.content.decode())
    
    def test_empty_genre(self):
        # adds a genre with no shows, checks what the response is
        genre = Genre.objects.get_or_create(name="test genre")
        response = self.client.get(reverse('TVShowApp:show_genre', kwargs={'genre_name_slug':'test-genre'}))
        lookupString = 'There are no shows in this genre.'
        self.assertIn(lookupString, response.content.decode())
        

class ShowViewTests(TestCase):
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('TVShowApp:tv_show',kwargs={'show_id':1}))
        self.content = self.response.content.decode()

    # checks that view returns correct data in context dictionary
    def test_show_context_dictionary(self):
        show = Show.objects.get(id=1)
        
        reviews = list(Review.objects.filter(show=show.id))
        belongings = list(Belonging.objects.filter(show=show))
        genres = []
        for belonging in belongings:
            genres.append(Genre.objects.get(name=belonging.genre))
        
        response_show_name = self.response.context['show']
        response_reviews = list(self.response.context['reviews'])
        response_show_genres = list(self.response.context['show_genres'])

        self.assertEquals(show,response_show_name)
        self.assertEquals(reviews,response_reviews)
        self.assertEquals(genres,response_show_genres)

     # is it using the correct template
    def test_show_template(self):
        self.assertTemplateUsed(self.response, 'TVShowApp/tv_show.html', f"The tv_show.html template isn't used")
   

class BadShowViewTests(TestCase):
    # tries to go to a nonexistent show, checks response
    def test_nonexistent_show(self):
        response = self.client.get(reverse('TVShowApp:tv_show',kwargs={'show_id':0}))
        lookupString = 'No show info available.'
        self.assertIn(lookupString, response.content.decode())
