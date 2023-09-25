from django.db import models
from django.contrib.auth.models import User

# create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # TODO: Define title, content, publish_date, and author fields here
