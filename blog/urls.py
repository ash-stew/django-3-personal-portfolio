
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.all_blogs, name='all_blogs'), # calling the home method in views.py
     path('<int:blog_id>/', views.detail, name='detail'), 
     # if anyone enters an int after blog, want to represent that int with name blog id and pass detail
]

