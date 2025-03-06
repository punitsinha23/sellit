from django.db import models
from django.contrib.auth.models import User
from djangoproject import settings
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    if settings.DEBUG:
        profile_picture = models.ImageField(upload_to='profile_pics/')
    else:     
        profile_picture = CloudinaryField('profile_pics') 

    def __str__(self):
        return f"{self.user.username}'s Profile"
