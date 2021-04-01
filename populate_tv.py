import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TVShowAppProject.settings')
django.setup()
from TVShowApp.models import Show, Genre, Belonging, Review
from django.contrib.auth.models import User
from pathlib import Path

def populate():
    
    BASE_DIR = Path(__file__).resolve().parent
    IMAGES_DIR = os.path.join(BASE_DIR,'media/show_images')

    users = [
        {'username':'test1',
         'password':'test1password'},
        {'username':'test2',
         'password':'test2password'},
        {'username':'test3',
         'password':'test3password'},
        {'username':'test4',
         'password':'test4password'}
    ]

    criminal_minds_reviews = [
        {'user':'test1',
         'comment':'This is a comment about Criminal Minds',
         'rating':10},
        {'user':'test2',
         'comment':'This is a comment about Criminal Minds',
         'rating':3}
    ]

    the_blacklist_reviews = [
        {'user':'test2',
         'comment':'This is a comment about The Blacklist',
         'rating':2},
        {'user':'test1',
         'comment':'This is a comment about The Blacklist',
         'rating':4},
        {'user':'test3',
         'comment':'This is a comment about The Blacklist',
         'rating':9},
        {'user':'test4',
         'comment':'This is a comment about The Blacklist',
         'rating':5}
    ]

    game_of_thrones_reviews = [
        {'user':'test3',
         'comment':'This is a comment about Game of Thrones',
         'rating':2},
        {'user':'test4',
         'comment':'This is a comment about Game of Thrones',
         'rating':10},
        {'user':'test1',
         'comment':'This is a comment about Game of Thrones',
         'rating':6}
    ]

    community_reviews = [
         {'user':'test1',
         'comment':'This is a comment about Community',
         'rating':3},
         {'user':'test4',
         'comment':'This is a comment about Community',
         'rating':8}
    ]

    buffy_the_vampire_slayer_reviews = [
        {'user':'test3',
         'comment':'This is a comment about Buffy the Vampire Slayer',
         'rating':2},
        {'user':'test4',
         'comment':'This is a comment about Buffy the Vampire Slayer',
         'rating':3},
        {'user':'test2',
         'comment':'This is a comment about Buffy the Vampire Slayer',
         'rating':5}
    ]

    shows = [
        {'title':'Criminal Minds',
         'year':2005,
         'genres':['Drama','Crime','Mystery'],
         'avg_rating': 6.5,
         'reviews':criminal_minds_reviews,
         'photo':os.path.join(IMAGES_DIR,'cm.jpg'),
         'reviewed':True,
         'likes':10},
        {'title':'Line of Duty',
         'year':2012,
         'genres':['Drama','Crime'],
         'avg_rating': 0.0,
         'photo':os.path.join(IMAGES_DIR,'lod.jpg'),
         'reviewed':True,
         'likes':1},
        {'title':'The Blacklist',
         'year':2013,
         'genres':['Drama','Crime'],
         'avg_rating': 5,
         'reviews':the_blacklist_reviews,
         'photo':os.path.join(IMAGES_DIR,'tb.jpg'),
         'reviewed':True,
         'likes':16},
        {'title':"Grey's Anatomy",
         'year':2005,
         'genres':['Drama'],
         'avg_rating': 0.0,
         'photo':os.path.join(IMAGES_DIR,'ga.jpg'),
         'reviewed':True,
         'likes':18},
        {'title': "Community",
         'year':2009,
         'genres':['Comedy'],
         'avg_rating':5.5,
         'reviews':community_reviews,
         'photo':os.path.join(IMAGES_DIR,'c.jpg'),
         'reviewed':True,
         'likes':4},
        {'title': "Game of Thrones",
         'year':2011,
         'genres':['Drama','Fantasy','Adventure'],
         'avg_rating':6,
         'reviews':game_of_thrones_reviews,
         'photo':os.path.join(IMAGES_DIR,'got.jpg'),
         'reviewed':True,
         'likes':24},
         {'title': "The Mandalorian",
         'year':2019,
         'genres':['Action','Sci-Fi'],
         'avg_rating':0.0,
         'photo':os.path.join(IMAGES_DIR,'tm.jpg'),
         'reviewed':True,
         'likes':22},
         {'title': "Buffy The Vampire Slayer",
         'year':1997,
         'genres':['Action','Fantasy','Drama'],
         'avg_rating':3.3,
         'reviews':buffy_the_vampire_slayer_reviews,
         'photo':os.path.join(IMAGES_DIR,'btvs.jpg'),
         'reviewed':True,
         'likes':11}
    ]
    
    for user in users:
        add_user(user['username'],user['password'])

    for show in shows:
        s = add_show(show['title'],show['year'],show['avg_rating'],show['photo'],show['reviewed'],show['likes'])
        for genre in show['genres']:
            g = add_genre(genre)
            add_belonging(s,g)
        if 'reviews' in show.keys():
            for review in show['reviews']:
                add_review(review['user'],s,review['comment'],review['rating'])
    
def add_belonging(show,genre):
    b = Belonging.objects.get_or_create(genre=genre, show=show)[0]
    b.save()
    return b

def add_show(title, year, avg_rating, photo, reviewed, likes):
    s = Show.objects.create(year=year,avg_rating = avg_rating, reviewed=reviewed, likes=likes)
    s.title = title
    s.photo = photo
    s.save()
    return s

def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

def add_review(user,show,comment,rating):
    u = User.objects.get(username=user)
    r = Review.objects.create(user=u,show=show,comment=comment,rating=rating)
    r.save()
    return r

def add_user(username, password):
    u = User.objects.create_user(username=username, password=password)
    return u

if __name__ == '__main__':
    print("Starting population script...")
    populate()