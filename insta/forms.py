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



