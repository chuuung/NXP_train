from django.db import models
from ultralytics import YOLO
class MyModel(models.Model):
    model = YOLO("best.pt")
# model = YOLO("best.pt")
# predict = model("pictures/PXL_20231020_034347462_jpg.rf.a6c5aa016718aabe0ec58ea77cd78815.jpg")
# print(len(predict[0].boxes.conf))