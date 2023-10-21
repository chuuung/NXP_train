from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import MyModel

# Create your views here.
 
def train(request):
    return render(request, 'train/train.html')


def predict(request):
    predict = MyModel.model("pictures/PXL_20231020_034347462_jpg.rf.a6c5aa016718aabe0ec58ea77cd78815.jpg")
    return JsonResponse({'result': len(predict[0].boxes.conf)})