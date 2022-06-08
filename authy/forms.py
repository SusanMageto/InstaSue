from django import forms
from authy.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class EditProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)

    class Meta:
        model = Profile
        fields = ['profile_photo',  'bio']



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    # username = forms.EmailInput(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']