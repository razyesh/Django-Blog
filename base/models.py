from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, related_name='post', on_delete=models.PROTECT)
    content = RichTextUploadingField()
    meta_content = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='post', on_delete= models.CASCADE)
    image = models.ImageField(default='home/images/default.png', upload_to = 'home/images')
    publish = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Posts'
        ordering = ['-datetime']


class Subscribe(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

