import logging
import os
from typing import Any

import torch as torch


# from src.config import FILE_ROOT_PATH
# from src.conv import convertHeicImage, transformImage

# files = os.listdir(f"{FILE_ROOT_PATH}/out")

# for f in files:
# Step 1: convert image
# name_after_conversion = convertHeicImage(f)

# Step 2: transform image to topdown view
# transformImage(f)


def recognize_model(image: str, model: Any):
    # Inference
    results = model(image)
    mower_coordinate = results.pandas().xyxy[0]
    return mower_coordinate


if __name__ == "__main__":
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    logger.info('running in local environment')

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/mower.pt', force_reload=True)
