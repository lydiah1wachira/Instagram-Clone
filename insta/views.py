from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404, HttpResponseRedirect
from .forms import CommentForm

# Create your views here.

def landing(request):
  '''
  view function to display the landing page and all of its data
  '''
  posts = Post.get_images().order_by('-date_posted')
  users = User.objects.exclude(id=request.user.id)
  current_user = request.user
  suggested_accounts = Profile.objects.all()

  return render(request, 'instapages/landing-page.html', {'posts':posts, 'users':users, 'current_user':current_user, 'suggested_accounts':suggested_accounts})


def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})

def post_comment(request, id):
    image = get_object_or_404(Post, pk=id)
    is_liked = False
    # if image.likes.filter(id=request.user.id).exists():
    #     is_liked = True
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
        # 'total_likes': image.total_likes()
    }
    return render(request, 'post.html', params) 