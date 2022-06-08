from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404, HttpResponseRedirect
from .forms import CommentForm,NewProfileForm,NewPostForm,UpdateUserProfileForm,UpdateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def landing(request):
  '''
  view function to display the landing page and all of its data
  '''
  posts = Post.get_images().order_by('-date_posted')
  users = User.objects.exclude(id=request.user.id)
  current_user = request.user
  suggested_accounts = Profile.objects.all()

  return render(request, 'instapages/landing-page.html', {'posts':posts, 'users':users, 'current_user':current_user, 'suggested_accounts':suggested_accounts})

@login_required
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('profile')

    else:
        form = NewProfileForm()
    return render(request,'new-profile.html', {"form": form})           

@login_required
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'instapages/search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'instapages/search.html', {'message': message})

@login_required
def profile(request,profile_id):
  
    images = request.user.profile.posts.all()
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'images' : images,   
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'profile.html', params)

@login_required
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    users = User.objects.get(username=username)
    
    id = request.user.id
    follow_status = None
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        
    }
    return render(request, 'user_profile.html', params)       

@login_required
def new_post(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
        return redirect('landing')

    else:
        form = NewPostForm()
    return render(request,'instapages/new_post.html', {"form": form})  


@login_required
def post_comment(request, id):
    image = get_object_or_404(Post, pk=id)
    current_user = request.user
    is_liked = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    params = {
        'image': image,
        'form': form,
        'is_liked': is_liked,
        
    }
    return render(request, 'comment.html', params) 



