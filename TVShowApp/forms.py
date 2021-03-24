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