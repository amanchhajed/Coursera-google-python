#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
image_directory = '/home/student-02-82bcc67d0a45/supplier-data/images/'
files = os.listdir(image_directory)
for image_name in files:
    if '.jpeg' in image_name:
        image_path = image_directory + image_name
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})