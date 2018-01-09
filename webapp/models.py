from django.db import models

# Create your models here.
class XgboostModel(models.Model):
    created = models.DateTimeField("date created")

class TrainingData(models.Model):
    created = models.DateTimeField("date created")
