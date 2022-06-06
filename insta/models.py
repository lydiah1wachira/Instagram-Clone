from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
  '''
  profile model class to help create news instances of the profile object.
  '''
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  profile_photo = models.ImageField(upload_to = 'profile/')
  bio = HTMLField(blank=True,default='I am a new user!')
  name = models.CharField(blank=True, max_length=60)



