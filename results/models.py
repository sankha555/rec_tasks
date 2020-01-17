from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length = 50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# Create your models here.
