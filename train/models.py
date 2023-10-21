from django.db import models
from ultralytics import YOLO

class MyModel(models.Model):
    model = YOLO("train/best.pt")
# Create your models here.
