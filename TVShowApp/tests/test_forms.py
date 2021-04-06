from django.forms import fields as django_fields
from django.test import TestCase
from TVShowApp.forms import GenreForm, UserForm, ShowForm, ReviewForm

class TestUserForm(TestCase):
    def test_user_form_exist(self):
        import TVShowApp.forms
        self.assertTrue('UserForm' in dir(TVShowApp.forms))

        from TVShowApp.forms import UserForm
        user_form = UserForm()
        
    # how form handles correct data
    def test_user_form_valid(self):
        form = UserForm(data={"username":"test1", "password":"test1password"})
        self.assertTrue(form.is_valid())

    # how form handles incorrect data
    def test_user_form_not_valid(self):
        form = UserForm(data={"username":"", "password":""})
        self.assertFalse(form.is_valid())
