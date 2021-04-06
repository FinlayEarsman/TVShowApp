from django.test import TestCase
from TVShowApp.models import Genre, Show, Belonging, Review
from django.http import HttpRequest
from django.urls import reverse
from populate_tv import populate


class ModelTests(TestCase):
    def setUp(self):
        populate()

    def test_genre_model(self):
        genre_sitcom = Genre.objects.get(name="Sitcom")
        self.assertEqual(genre_sitcom.name, "Sitcom")
        
    def test_str_method_genre(self):
        genre_sitcom = Genre.objects.get(name="Sitcom")
        self.assertEqual(str(genre_sitcom), 'Sitcom')       

    def test_show_model(self):
        show = Show.objects.get(title='Modern Family')
        self.assertEquals(show.year, 2009)
        self.assertEquals(show.title, "Modern Family")

    def test_str_method_show(self):        
        show = Show.objects.get(title='Modern Family')       
        self.assertEqual(str(show), 'Modern Family')
        


        


        

    
        
        
