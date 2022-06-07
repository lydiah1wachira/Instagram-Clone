from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


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

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)
          

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      try:
          instance.profile.save()
      except ObjectDoesNotExist:
          Profile.objects.create(user=instance)
  
  @classmethod
  def search_profile(cls, name):
      return cls.objects.filter(user__username__icontains=name).all() 


class Post(models.Model):
    '''
    Post model class to help create new instances of a post object
    '''
    image = models.ImageField(upload_to ='posts/')
    image_name = models.CharField(max_length=40)
    image_caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    image_likes = models.PositiveIntegerField(default=0,blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 
    
    @classmethod
    def search_by_caption(cls,search_term):
        post = cls.objects.filter(caption__icontains=search_term)
        return post

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @classmethod
    def filter_images_by_user(cls,id):
        images_by_user = cls.objects.filter(profile = id).all() 
        return images_by_user    
    
      
class Comment(models.Model):
    '''
    Comment model class to help create new instances of a comment object
    '''
    content = HTMLField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ["-pk"]

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image_id=id)
        return comments   