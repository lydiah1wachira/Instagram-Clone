from django.test import TestCase
from .models import Post,Profile
from datetime import datetime
from django.contrib.auth.models import User

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.test_user= User(username = "wachira", password = "severussnape")
        self.test_user.save()

        self.test_image = Post(image='images/test.jpg', posted_by=self.test_user, date_posted=datetime.now())

    def test_instance(self):
        self.assertTrue(isinstance(self.test_image,Post))

    def test_save(self):
        self.test_image.save()
        self.assertEqual(len(Post.objects.all()), 1)

    def tearDown(self):
        self.test_user.delete() 
        Post.objects.all().delete()   

class ProfileTest(TestCase):
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Felista')

    def tearDown(self):
        self.user.delete()

    def test_profile_creation(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)   