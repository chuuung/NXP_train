from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import MyModel
from ultralytics import YOLO
import os
import json
from pathlib import Path

# Create your views here.
INI_temperature = 27
context = {
    't1' : {"t":INI_temperature, "p": 1},
    't2' : {"t":INI_temperature, "p": 1},
    't3' : {"t":INI_temperature, "p": 1},
    't4' : {"t":INI_temperature, "p": 5},
}

def check_number():
    PICTURES_DIR = "train/pictures"
    all_path = list(Path(PICTURES_DIR).glob("**/*.jpg"))
    print(all_path)
    print(all_path[0].parent.name)
    for file_path in all_path:
        predict = MyModel.model(file_path)

        context[file_path.parent.name]["p"] = len(predict[0].boxes.conf)
        # predict = MyModel.model("train/pictures/t1/PXL_20231020_034347462_jpg.rf.a6c5aa016718aabe0ec58ea77cd78815.jpg")

    # predict = MyModel.model("train/pictures/t1/PXL_20231020_034347462_jpg.rf.a6c5aa016718aabe0ec58ea77cd78815.jpg")
    # context['p1']["p"] = len(predict[0].boxes.conf)


def train(request):
    check_number()
    return render(request, 'train/train.html',context=context)

def feedback(request):
    return render(request, 'train/feedback.html')

