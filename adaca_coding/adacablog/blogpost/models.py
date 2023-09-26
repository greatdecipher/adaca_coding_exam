from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"Title: {self.title}"
    

    # TODO: Define title, content, publish_date, and author fields here
