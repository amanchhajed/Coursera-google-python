#!/usr/bin/env python3
from PIL import Image
import os
image_directory = '/home/student-02-82bcc67d0a45/supplier-data/images/'
files = os.listdir(image_directory)
for image_name in files:
    if 'tiff' in image_name:
        image_path = image_directory + image_name
        im = Image.open(image_path)
        new_path = image_path.replace(".tiff", ".jpeg")
        im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")