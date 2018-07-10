from django.test import TestCase
from .forms import SignUpForm


# Create your tests here.
class CoreFormTest(TestCase):
    def setUp(self):
        form = SignUpForm({
            'username': 'johndoe',
            'email': 'johndoe@gmail.com',
            'password1': 'topper234',
            'password2': 'topper234'
        })

        form.save()

    def test_blank_data(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())

    def test_password_does_not_match_error(self):
        form = SignUpForm({
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testpass',
            'password2': 'testpassone'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'password2': ['The two password fields didn\'t match.']
        })

    def test_duplicated_username_throws_error(self):
        form = SignUpForm({
            'username': 'johndoe',
            'email': 'jdoe@gmail.com',
            'password1': 'potter123',
            'password2': 'potter123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['A user with that username already exists.']
        })

    def test_duplicated_email_throws_error(self):
        form = SignUpForm({
            'username': 'jdoe',
            'email': 'johndoe@gmail.com',
            'password1': 'potter123',
            'password2': 'potter123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'email': ['Email already exists']
        })

