from django.db import models
from django.urls import reverse
import os
from datetime import datetime
from django.contrib.auth.models import Permission



# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя разрабочика")
    description = models.TextField(blank=True)  # поле описания

    def get_absolute_url(self):
        return reverse("develop-detail", args=[str(self.id)])


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(verbose_name="Описание проекта")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("section-detail.html", args=[str(self.id)])




class Card(models.Model):
    name = models.CharField(max_length=50)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    description = models.TextField()
    image_file = models.ImageField(upload_to="cards/", blank=True)
    section = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name





class Manager(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)  # поле описания

    def get_absolute_url(self):
        return reverse("develop-detail", args=[str(self.id)])

