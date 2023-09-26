from django.urls import path
from . import views

urlpatterns = [
    path('blogpost', views.get_latest_posts),
    path('create/', views.create_post, name='create')

]