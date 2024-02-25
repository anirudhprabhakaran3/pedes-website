from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.email


class ActivityLog(models.Model):
    ip = models.CharField(max_length=20, blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.ip
