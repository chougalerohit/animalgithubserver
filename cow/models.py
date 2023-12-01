from django.db import models

# Create your models here.

class cow_info_model(models.Model):

    name = models.CharField(max_length=30)
    milk = models.FloatField()
    color = models.CharField(max_length=20)