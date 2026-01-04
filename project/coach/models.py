from django.db import models

class Coach(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='coach/images/')
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)


    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description or "Photo"