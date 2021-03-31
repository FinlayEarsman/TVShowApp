from django import forms
from django.forms import Textarea
from TVShowApp.models import Genre, Review, Show
from django.contrib.auth.models import User


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=Genre.NAME_MAX_LENGTH, help_text="Please enter the name of the new genre.")

    class Meta:
        model = Genre
        fields = ('name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ShowForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the title of the show.")
    year = forms.IntegerField(help_text="Please enter the year of the show.")
    photo = forms.ImageField(help_text="Please upload a photo for the show.")

    class Meta:
        model = Show
        fields = ('title', 'year', 'photo', 'avg_rating', 'reviewed')


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=Textarea(attrs={'rows': '2', 'cols': '30'}), label="Comment:", required=False)
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'step': 1, 'max': 10, 'min': 1}))

    class Meta:
        model = Review
        fields = ('comment', 'rating')
