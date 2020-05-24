from django.db import models
from django.contrib.postgres.fields import ArrayField

class MyInfo(models.Model):
    about_me = models.TextField()
    skills = ArrayField(models.CharField(max_length=30))
    certs = ArrayField(models.TextField())


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email_id = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
