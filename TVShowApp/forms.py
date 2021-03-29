from django import forms
from TVShowApp.models import Genre
from django.contrib.auth.models import User


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=Genre.NAME_MAX_LENGTH,
                           help_text="Please enter the name of the new genre.")

    # An inline class to provide
    class Meta:
        # Provide an association
        model = Genre
        fields = ('name',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password',)

class ShowForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                           help_text="Please enter the titke of the show.")
    year = forms.IntegerField(help_text="Please enter the year of the show.")
    photo = forms.ImageField(help_text="Please upload a photo for the show.")
    avg_rating = forms.FloatField(help_text="Please enter the rate of the show.")


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(max_length=500)
    rating = forms.IntegerField()

