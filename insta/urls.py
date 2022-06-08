from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.landing, name='landing' ),
  path('search/', views.search_profile, name='search'),
  re_path(r'comment/<id>', views.post_comment, name='comment'),
  path('new/post/', views.new_post, name='new-post'),
  path('new/profile/', views.new_profile, name='new-profile'),
  re_path(r'profile/(?P<profile_id>\d+)', views.profile, name='profile'),
  re_path(r'user_profile/(?P<username>\w+)', views.user_profile, name='user_profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)