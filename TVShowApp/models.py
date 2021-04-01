from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Genre(models.Model):
    NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Show(models.Model):
    title = models.CharField(max_length=100)                       #Title of TV Show
    year = models.IntegerField()                                   #Year of Release
    photo = models.ImageField(upload_to="show_images", blank=True) #Photo/Poster of Show
    avg_rating = models.FloatField(default=0)                      #Average Rating Across All User Reviews
    reviewed = models.BooleanField(default=False)                  #Has the show been marked as correct by an admin?
    likes = models.IntegerField(blank=False, default=0)            #How many likes does the show have

    def __str__(self):
        return self.title


class Belonging(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.show}({self.genre})"


class Review(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user}'s review of {self.show}"
