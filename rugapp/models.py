from django.db import models

# Create your models here.

class NFTProject(models.Model):
    description_text = models.CharField(max_length=200)
    title = models.CharField(max_length=200)