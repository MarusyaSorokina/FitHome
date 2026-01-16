from django.db import models

from programs.models import Exercise, Photo

class CoachCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Программа')
    description = models.TextField(blank=True, verbose_name='Описание программы')


class Coach(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название упражнения")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='program_images/', blank=True,verbose_name="Изображение")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'


class Photo(models.Model):
    image = models.ImageField(upload_to='program_images/add/', blank=True, verbose_name="Фото")
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'