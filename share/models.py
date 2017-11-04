from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# This code is triggered whenever a new user has been created and saved to the database
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=100,db_index=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=50,db_index=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

class PostImage(models.Model):
    post = models.ForeignKey(Post)
    image = models.FileField(upload_to='static/')
    created_timestamp = models.DateTimeField(auto_now_add=True)




