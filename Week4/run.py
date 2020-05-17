#!/usr/bin/env python3
import os
import json
import locale
import requests

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
description_directory = '/home/student-02-82bcc67d0a45/supplier-data/descriptions/'
description_files = os.listdir(description_directory)
image_directory = '/home/student-02-82bcc67d0a45/supplier-data/images/'
url = "http://localhost/fruits/"

for description_name in description_files:
    if '.txt' in description_name:
        description_path = description_directory + description_name
        image_name = description_name.replace(".txt", ".jpeg")
        with open(description_path) as content:
            data = content.readlines()
            name = data[0].strip('\n')
            weight = int(data[1].strip('\n').replace(' lbs', ""))
            description = data[2].strip('\n')
            catalog_object = {"name": "{}".format(name), "weight": weight,
                              "description": "{}".format(description.replace(u'\xa0', u'')),
                              "image_name": "{}".format(image_name)}
            dict_to_json = json.dumps(catalog_object)
            header = {'Content-Type': 'application/json'}
            requests.post(url, headers=header, data=dict_to_json)