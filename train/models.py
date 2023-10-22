from django.db import models
from ultralytics import YOLO

class MyModel(models.Model):
    model = YOLO("train/best.pt")
# Create your models here.

class Feedback(models.Model):
    #idx = models.BigAutoField()
    #train_id = models.IntegerField()
    temp = models.CharField(max_length = 2)
    OtherRequest = models.CharField(max_length = 100)