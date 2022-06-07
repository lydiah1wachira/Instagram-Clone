from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.landing, name='landing' ),
  path('search/', views.search_profile, name='search'),
  path('comment/<id>', views.post_comment, name='comment'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)