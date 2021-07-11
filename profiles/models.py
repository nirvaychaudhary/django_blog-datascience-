from django.db import models
from accounts.models import CustomUser
# # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatar/')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
