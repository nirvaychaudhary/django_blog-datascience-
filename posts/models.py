from django.db import models
from accounts.models import CustomUser
from profiles.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    liked = models.ManyToManyField(CustomUser, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title