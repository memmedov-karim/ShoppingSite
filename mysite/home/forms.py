from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, FileInput, Select, TextInput, Textarea

from home.models import UserProfileInfo
class SearchForm(forms.Form):
    query = forms.CharField(label='serach',max_length=100)
    catid = forms.CharField()
class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30,label='User Name')
    email=forms.EmailField(max_length=40,label='Email')
    first_name=forms.CharField(max_length=30, help_text='First Name', label='First Name')
    last_name=forms.CharField(max_length=30, help_text='Last Name', label='Last Name')
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2',]
class UserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email',]
        widgets = {
            'username': TextInput(attrs={'class':'input','placeholder':'username'}),
            'email': EmailInput(attrs={'class':'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class':'input','placeholder':'first_name'}),
            'last_name': Textarea(attrs={'class':'input','placeholder':'last_name'}),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields = ['phone','city','country','image','address',]
        userprofile = {
            'phone': TextInput(attrs={'class':'input','placeholder':'phone'}),
            'country': Select(attrs={'class':'input','placeholder':'country'}),
            'address': TextInput(attrs={'class':'input','placeholder':'address'}),
            'city': TextInput(attrs={'class':'input','placeholder':'city'}),
            'image': FileInput(attrs={'class':'input','placeholder':'image'}),

        }

