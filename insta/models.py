from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
  '''
  Model class to help create new instances of a profile object
  '''
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  profile_photo = models.ImageField( upload_to = 'profile/', blank=True)
  bio = HTMLField(blank=True,default='I am a new user!')
  name = models.CharField(blank=True, max_length=60)
