from django.db import models
from datetime import datetime

# Create your models here.
#make migrations to database with every change in models.py

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 1000000)
    created_at = models.DateTimeField(default = datetime.now(), blank = True)