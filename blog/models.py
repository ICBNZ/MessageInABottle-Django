from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model
from accounts.models import Address
from settings import AUTH_USER_MODEL
from django.urls import reverse

User = user_model()

class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    image = models.ImageField(upload_to='media', default='media/beach_pollution.jpg',
    null=True, blank=True)
    datePublished = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes= models.ManyToManyField(AUTH_USER_MODEL, blank=True, related_name="post_likes",)
    commentsTotal = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse("comment_section", kwargs={"postid":self.id})

    def get_like_url(self):
        return reverse("like-toggle", kwargs={"id": self.id})

    def like_api_url(self):
        return reverse("like-api", kwargs={"id": self.id})

    def __str__(self):
        return "Post ID: " + str(self.id) + ", Title: " + self.title + ", Author: " + self.user.username + ", Date: " + self.datePublished.strftime("%m/%d/%Y")


class Event(models.Model):
    title = models.CharField(max_length=55)
    details = models.TextField()
    dateTime = models.DateTimeField()
    image = models.ImageField(upload_to='user_image/', default='user_image/beach.jpg',
    null=True, blank=True)
    addressID = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Event ID: " + str(self.id) + ", Title: " + self.title + ", Author: " + self.userId.username + ", Date: " + self.dateTime.strftime("%m/%d/%Y")

class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentTime =  models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return "Comment ID: " + str(self.id) + ", Author: " + self.userId.username + ", Date: " + self.commentTime.strftime("%m/%d/%Y")
