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

  def save_profile(self):
        self.save() 

  def delete_profile(self):
      self.delete()

  def update_bio(self,new_bio):
      self.bio = new_bio
      self.save()

  def update_image(self, user_id, new_image):
      user = User.objects.get(id = user_id)
      self.photo = new_image 
      self.save()              
