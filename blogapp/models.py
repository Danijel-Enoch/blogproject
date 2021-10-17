from django.db import models
from django.contrib.auth.models import User

Status=((0,"draft"),(1,"published"))

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    content=models.TextField()
    status=models.IntegerField(choices=Status, default=0)

    class meta:
        ordering=['-created_on']
    
    def _str_(self):
        return self.title

