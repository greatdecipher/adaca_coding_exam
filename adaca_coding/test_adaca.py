"""
Technical Test: Senior Software Developer - Python & Django

Complete the code tasks below. Remember to consider best practices and the principles of clean, efficient code.

Your code will be evaluated based on correctness, efficiency, readability, and best practices.
"""

# 1. Python Fundamentals

# 1.1. Complete the function below.
def max_repeat(numbers):
    """
    Given a list of integers, return the integer with the maximum number of repeated digits.
    """
    string_number_list = []
    for num in numbers:
        string_number_list.append(str(num))

    

assert max_repeat([123, 1123, 332, 4445, 5566]) == 4445


# 2. Django Fundamentals

# Assuming you have Django environment set up:

# 2.1. Create a Django model for a `BlogPost`.

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    # TODO: Define title, content, publish_date, and author fields here
    pass


# 3. Django ORM & Databases

# 3.1. Given the BlogPost model above, retrieve all BlogPosts written by a User with username 'john_doe'.
# Write the query below:

# posts_by_john = ?

# 3.2. Optimize the following view function for better performance:
from django.shortcuts import render
def get_latest_posts(request):
    posts = BlogPost.objects.all().order_by('-publish_date')[:10]
    # TODO: Optimize the above line for better performance.
    return render(request, 'latest_posts.html', {'posts': posts})


# 4. Django Forms & Validation

from django import forms

# 4.1. Create a Django form for submitting a BlogPost.

class BlogPostForm(forms.ModelForm):
    # TODO: Ensure title is not more than 200 characters and content is not empty.
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'publish_date', 'author']


# 5. Advanced Django Topics

# 5.1. Implement a Django middleware to record the response time of every request.

from datetime import datetime
from django.http import HttpResponse

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        response = self.get_response(request)
        # TODO: Calculate and print response time for the request.
        return response


# 6. Practical Application

# 6.1. Using the Django ORM, write a function that returns the title of the most recent BlogPost.

def get_latest_blog_title():
    pass

# Test your function
# assert get_latest_blog_title() == "Your most recent blog's title"

