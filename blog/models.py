from django.db import models
import re
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    STATE_CHOICES = [
        ('PUBLISHED', 'PUBLISHED'),
        ('DRAFT', 'DRAFT')
    ]
    title = models.CharField(max_length=255, unique=True, blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ImageField(blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='DRAFT')
    hyperlink = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class PostSection(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='postsimg', blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    type = models.ForeignKey('SectionType', models.SET_NULL, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    command = models.TextField(blank=True)
    error = models.TextField(blank=True)
    hyperlink = models.TextField(blank=True)

    def __str__(self):
        return self.title

class  SectionType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type
