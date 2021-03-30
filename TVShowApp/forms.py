from django import forms
from django.contrib.postgres.forms import RangeWidget
from django.forms import NumberInput, Textarea
from TVShowApp.models import Genre, Review
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
        fields = ('username', 'email', 'password',)


class ShowForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            help_text="Please enter the title of the show.")
    year = forms.IntegerField(help_text="Please enter the year of the show.")
    photo = forms.ImageField(help_text="Please upload a photo for the show.")
    avg_rating = forms.FloatField(help_text="Please enter the rate of the show.")


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=Textarea(attrs={'rows': '2', 'cols': '30'}), label="Comment:")
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'step': 1, 'max': 10, 'min': 1}))

    class Meta:
        model = Review
        fields = ('comment', 'rating')
