from django.db import models

class TrainData(models.Model):
    idx = models.IntegerField() # Primary Key
    image = models.BinaryField()
    label = models.IntegerField()

# class TestData(models.Model):
#     image = models.BinaryField()
#     label = models.IntegerField()
