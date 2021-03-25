from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Genre(models.Model):
    NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args,**kwargs)

    def __str__(self):
        return self.name


class Show(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    photo = models.ImageField(upload_to="show_images", blank=True)
    avg_rating = models.FloatField()

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
    id = models.IntegerField(unique=True, primary_key=True)
    comment = models.CharField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user}'s review of {self.show}"
