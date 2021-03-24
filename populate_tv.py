import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TVShowAppProject.settings')
import django
django.setup()
from TVShowApp.models import Show, Genre, Belonging, Review





def populate():

    shows = [
        {'title':'Criminal Minds',
         'id':'0001',
         'year':2005,
         'genres':['Drama','Crime','Mystery'],
         'avg_rating': 5.0},
        {'title':'Line of Duty',
         'id':'0002',
         'year':2012,
         'genres':['Drama','Crime'],
         'avg_rating': 4.4},
        {'title':'The Blacklist',
         'id':'0003',
         'year':2013,
         'genres':['Drama','Crime'],
         'avg_rating': 2.9},
        {'title':"Grey's Anatomy",
         'id':'0004',
         'year':2005,
         'genres':['Drama'],
         'avg_rating': 3.6},
        {'title': "Community",
         'id':'0005',
         'year':2009,
         'genres':['Comedy'],
         'avg_rating':3.5},
        {'title': "Game of Thrones",
         'id':'0006',
         'year':2011,
         'genres':['Drama','Fantasy','Adventure'],
         'avg_rating':1.8},
         {'title': "The Mandalorian",
         'id':'0007',
         'year':2019,
         'genres':['Action','Sci-Fi'],
         'avg_rating':4.1},
         {'title': "Buffy The Vampire Slayer",
         'id':'0008',
         'year':1997,
         'genres':['Action','Fantasy','Drama'],
         'avg_rating':4.6},
    ]
    
    for show in shows:
        s = add_show(show['id'], show['title'], show['year'],show['avg_rating'])
        for genre in show['genres']:
            g = add_genre(genre)
            add_belonging(s,g)
    
def add_belonging(show,genre):
    b = Belonging.objects.get_or_create(genre=genre, show=show)[0]
    b.save()
    return b

def add_show(id, title, year, avg_rating):
    s = Show.objects.get_or_create(id=id, year=year,avg_rating = avg_rating)[0]
    s.title = title
    s.save()
    return s

def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

if __name__ == '__main__':
    print("Starting population script...")
    populate()