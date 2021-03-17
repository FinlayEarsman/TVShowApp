from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name

class Show(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    photo = models.ImageField(upload_to="show_images" ,blank=True)

    def __str__(self):
        return self.title

class Belonging(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

class Review(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(unique=True,primary_key=True)
    comment = models.CharField(max_length = 500)
    rating = models.IntegerField()