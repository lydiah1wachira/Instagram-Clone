from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.landing, name='landing' ),
  path('search/', views.search_results, name='search_results'),
]