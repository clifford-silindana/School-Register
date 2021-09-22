from django.db import models

# Create your models here.

class Learner(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    grade = models.IntegerField()
    educator = models.CharField(max_length = 100)
    