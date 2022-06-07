from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from django.contrib.auth.models import User

# Create your views here.

def landing(request):
  '''
  view function to display the landing page and all of its data
  '''
  posts = Post.get_images().order_by('-date_posted')
  users = User.objects.exclude(id=request.user.id)
  current_user = request.user
  suggested_accounts = Profile.objects.all()

  return render(request, 'instagram/landing-page.html', {'posts':posts, 'users':users, 'current_user':current_user, 'suggested_accounts':suggested_accounts})
