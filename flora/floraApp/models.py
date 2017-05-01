from django.db import models

# Create your models here.
class Plant(models.Model):
    image = models.CharField(max_length=60)
    description = models.TextField()

class Language(models.Model):
    name = models.CharField(max_length=30)

class PlantName(models.Model):
    name = models.CharField(max_length=30)
    Plant = models.ForeignKey(Plant)
    Language = models.ForeignKey(Language)
