from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"
    

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Topic)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
# Create your models here.
