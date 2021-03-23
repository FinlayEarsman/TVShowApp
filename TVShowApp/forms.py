from django import forms
from TVShowApp.models import Genre


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=Genre.NAME_MAX_LENGTH,
                           help_text="Please enter the name of the new genre.")

    # An inline class to provide
    class Meta:
        # Provide an association
        model = Genre
        fields = ('name',)
