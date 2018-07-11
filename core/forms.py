from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, EmailField, ValidationError


class UniqueUserEmailField(EmailField):
    """
    An EmailField which only is valid if no user has that email
    """
    def validate(self, value):
        super(EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
            raise ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise ValidationError("Email already exists")
        except User.DoesNotExist:
            pass


class SignUpForm(UserCreationForm):
    email = UniqueUserEmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'class': 'input'
        })
        self.fields['email'].widget = EmailInput(attrs={
            'class': 'input'
        })
        self.fields['password1'].widget = PasswordInput(attrs={
            'class': 'input'
        })
        self.fields['password2'].widget = PasswordInput(attrs={
            'class': 'input'
        })

