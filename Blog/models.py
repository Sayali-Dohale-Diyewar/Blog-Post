from django.utils import timezone # type: ignore
from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser
from . import manager


# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=70, unique=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Default set to timezone.now without parentheses
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates to current time on save

    def __str__(self):
        return self.title


class Comment(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments" )  # ForeignKey to Posts model with related_name for reverse query
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Default set to timezone.now without parentheses
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates to current time on save

    def __str__(self):
        return self.posts.title


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")  # ForeignKey to Comment model with related_name for reverse query
    reply = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Default set to timezone.now without parentheses
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates to current time on save

    def __str__(self):
        return str(self.comment)
    
class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to='images')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = manager.UserManger()

    def __str__(self):
        return self.email
        