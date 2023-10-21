# from django.db import models
# from ultralytics import YOLO
# import json

# info_dict = {
#     "passengers": 0
# }

# model = YOLO("train/best.pt")
# predict = model("train/pictures/PXL_20231020_034347462_jpg.rf.a6c5aa016718aabe0ec58ea77cd78815.jpg")
# info_dict["passengers"] = len(predict[0].boxes.conf)
# json_object = json.dumps(info_dict)
# with open("test.json", "w") as outfile:
#     outfile.write(json_object)
