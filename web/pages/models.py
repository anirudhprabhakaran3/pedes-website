from django.db import models


# Create your models here.

class Announcement(models.Model):
    content = models.TextField()
    url = models.URLField(blank=True, null=True)


class Attende(models.Model):
    NATIONALITY_CHOICES = [
        ('IN', 'Indian'),
        ('FR', 'Foreign'),
    ]

    CATEGORY_CHOICES = [
        ('AUTHOR', 'Author'),
        ('STUDENT', 'Student'),
        ('PROF_ATN', 'Professional Attende'),
        ('AUTHOR_ATN', 'Author Attende'),
        ('TUTORIAL', 'Tutorial'),
    ]

    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES, default='Indian')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='Student')
    payment_check = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.get_nationality_display()} - {self.get_category_display()}"