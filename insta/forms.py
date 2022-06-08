from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment


class CommentForm(forms.ModelForm):
  '''Comment form class'''
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget = forms.TextInput()
        self.fields['content'].widget.attrs['placeholder'] = 'Add a comment...'

  class Meta:
      model = Comment
      fields = ('content',)

class NewProfileForm(forms.ModelForm):
  '''New Profile form class to help create profile objects'''
  class Meta:
        model = Profile
        exclude = ['user']


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name','profile_photo', 'bio']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted_by','date_posted', 'image_likes','user']



