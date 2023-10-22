from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from .models import MyModel
from .forms import FeedbackForm
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
    't4' : {"t":INI_temperature, "p": 30},
    't3_m':[]
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

def calculate_load():
    #standard temperture
    standard_t = 25
    area_btu = 23.5 * 3.2 * 3.6 * 31.25
    #area_btu = 18000
    light_btu = 3 * 4.25
    heat_load = 0
    ac = 2400
    a = 18000/ac
    b = 0.005
    for i in context:
        if i == "t3_m":
            break
        print(type(i))
        print(i)
        occupant_btu = context[i]["p"] * 600
        #occupant_btu = i['p'] * 600
        heat_load = area_btu + light_btu + occupant_btu
        #caculate heat load
    
        #heat_load = ac * a + (context[i]['p'] - 5) * d
        d = (heat_load - ac * a)/context[i]['p']
        #caculate cooling capacity

        new_t = INI_temperature - b * d
        if new_t > 28:
            new_t = 28.0
        elif new_t < 23:
            new_t = 23.0
        
        context[i]['t'] = round(new_t, 2)


def train(request):
    check_number()
    calculate_load()
    return render(request, 'train/train.html',context=context)

def feedback(request):
    form = FeedbackForm()
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        print("POST")
        h = request.POST.get("hot")
        c = request.POST.get("cold")
        print("Hot",request.POST.get("hot"))
        print("Cold",type(request.POST.get("cold")))
        state = ""
        if h == "on" and c == None:
            state = "H"
        elif c == "on" and h == None:
            state = "C"
        print(state)
        r = request.POST.get("OtherRequest")
        print(r)
        #form['temp'] = state
        form = FeedbackForm(request.POST)
        f = form.save(commit=False)
        f.temp = state
        f.OtherRequest = r
        f.save()
        #form['OtherRequest'] = r
        '''if form.is_valid:
            form.save()'''
        '''form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")'''
        #return render(request, 'train/feedback.html', {'form': form})
        if len(context["t3_m"]) >= 5:
            context["t3_m"].pop()
        context["t3_m"].append(r)
        return HttpResponseRedirect("/train/")
    
    else:
        #form = FeedbackForm()
        return render(request, 'train/feedback.html', {'form': form})

