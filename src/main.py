import os


import torch as torch

# from src.config import FILE_ROOT_PATH
# from src.conv import convertHeicImage, transformImage

# files = os.listdir(f"{FILE_ROOT_PATH}/out")

# for f in files:
    # Step 1: convert image
    # name_after_conversion = convertHeicImage(f)

    # Step 2: transform image to topdown view
    # transformImage(f)


model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/mower.pt', force_reload=True)

# Image
im = './test_file.jpg'

# Inference
results = model(im)

print( results.pandas().xyxy[0] )

