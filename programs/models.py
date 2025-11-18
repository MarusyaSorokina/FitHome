from django.db import models

class Programs(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    exercise = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='programs/images/')
    url = models.URLField(blank=True)

