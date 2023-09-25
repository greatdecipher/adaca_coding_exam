# 3.2. Optimize the following view function for better performance:
from django.shortcuts import render
from .models import BlogPost

def get_latest_posts(request):
    posts = BlogPost.objects.all().order_by('-publish_date')[:10]
    # TODO: Optimize the above line for better performance.
    return render(request, 'latest_posts.html', {'posts': posts})
