from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # inherits from UserCreationForm and adds email
    email = forms.EmailField()

    # Whenever this form is used it will create a new user
    # gives nested name space
    class Meta:
        model = User
        # fields shown on the form and what order
        fields = ['username', 'email', 'password1', 'password2']

# Create form to work witth specific db model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # fields shown on the form and what order
        fields = ['username', 'email']

# updates image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
