from django.shortcuts import render, HttpResponse

# Create your views here.
 
def train(request):
    return render(request, 'train/train.html')