import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TVShowAppProject.settings')
django.setup()
from TVShowApp.models import Show, Genre, Belonging, Review
from django.contrib.auth.models import User

def populate():

    shows = [
        {'title':'Criminal Minds',
         'id':'1',
         'year':2005,
         'genres':['Drama','Crime','Mystery'],
         'avg_rating': 5.0},
        {'title':'Line of Duty',
         'id':'2',
         'year':2012,
         'genres':['Drama','Crime'],
         'avg_rating': 4.4},
        {'title':'The Blacklist',
         'id':'3',
         'year':2013,
         'genres':['Drama','Crime'],
         'avg_rating': 2.9},
        {'title':"Grey's Anatomy",
         'id':'4',
         'year':2005,
         'genres':['Drama'],
         'avg_rating': 3.6},
        {'title': "Community",
         'id':'5',
         'year':2009,
         'genres':['Comedy'],
         'avg_rating':3.5},
        {'title': "Game of Thrones",
         'id':'6',
         'year':2011,
         'genres':['Drama','Fantasy','Adventure'],
         'avg_rating':1.8},
         {'title': "The Mandalorian",
         'id':'7',
         'year':2019,
         'genres':['Action','Sci-Fi'],
         'avg_rating':4.1},
         {'title': "Buffy The Vampire Slayer",
         'id':'8',
         'year':1997,
         'genres':['Action','Fantasy','Drama'],
         'avg_rating':4.6},
    ]

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

    reviews = [
        {'show':"0001",
         'user':'test1',
         'comment':'This is a comment about Criminal Minds',
         'rating':5,
         'id':1},
        {'show':"0001",
         'user':'test2',
         'comment':'This is a comment about Criminal Minds',
         'rating':3,
         'id':2},
        {'show':"0003",
         'user':'test2',
         'comment':'This is a comment about The Blacklist',
         'rating':4,
         'id':3},
        {'show':"0006",
         'user':'test3',
         'comment':'This is a comment about Game of Thrones',
         'rating':1,
         'id':4},
         {'show':"0005",
         'user':'test1',
         'comment':'This is a comment about Community',
         'rating':3,
         'id':5}
    ]
    
    for user in users:
        add_user(user['username'],user['password'])

    for show in shows:
        s = add_show(show['id'], show['title'], show['year'],show['avg_rating'])
        for genre in show['genres']:
            g = add_genre(genre)
            add_belonging(s,g)

    for review in reviews:
        add_review(review['id'],review['user'],review['show'],review['comment'],review['rating'],)
    
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

def add_review(id,user,show,comment,rating):
    u = User.objects.get(username=user)
    s = Show.objects.get(id=show)
    r = Review.objects.get_or_create(id=id,user=u,show=s,comment=comment,rating=rating)[0]
    r.save()
    return r

def add_user(username, password):
    u = User.objects.create_user(username=username, password=password)
    return u

if __name__ == '__main__':
    print("Starting population script...")
    populate()