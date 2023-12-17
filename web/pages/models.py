from django.db import models


# Create your models here.

class Announcement(models.Model):
    content = models.TextField()
    url = models.URLField(blank=True, null=True)
