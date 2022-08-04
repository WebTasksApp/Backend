from django.db import models
from django.contrib.auth.models import AbstractUser
from todo.models import Task

class User(AbstractUser):
    tasks = models.ManyToManyField(Task, null=True)
    #email = models.EmailField(unique=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []


