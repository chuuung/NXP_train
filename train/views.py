from django.shortcuts import render, HttpResponse

# Create your views here.
context = {
    'p1' : 1,
    'p2' : 2,
    'p3' : 3,
    'p4' : 15,
}

def train(request):
    return render(request, 'train/train.html',context=context)