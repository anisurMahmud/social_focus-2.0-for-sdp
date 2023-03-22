from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default = 'Default.png')
    location = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def _str_(self):
        return self.user

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def _str_(self):
        return self.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def _str_(self):
        return self.user
    




# messege part
class ThreadModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class MessageModel(models.Model):
	thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	body = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='uploads/message_photos', blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)
	is_read = models.BooleanField(default=False)