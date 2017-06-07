from __future__ import unicode_literals
from django.contrib.auth.models import User #import user, chapter 11
from django.db import models

# Create your models here.

class Project(models.Model): #I am making a collection of projects, rather than a collection of things. Added Chapter
    name = models.CharField(max_length=255) #define name of project(thing in book).  Chapter 6
    description = models.TextField() #define description of project(thing in book).  Chapter 6
    slug = models.SlugField(unique=True) #define slug of project(thing in book). Chapter 6
    user = models.OneToOneField(User, blank=True, null=True) #user model added Chapter 11
