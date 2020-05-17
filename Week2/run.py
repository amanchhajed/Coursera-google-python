#! /usr/bin/env python3

import os
import requests

dir_path = "/data/feedback/"
url='http://35.238.238.42/feedback/'
files = os.listdir(dir_path)
for file in files:
    data_dict = {}
    abs_path = dir_path + file
    with open(abs_path) as file_:
        lines = file_.readlines()
        data_dict["title"] = lines[0].rstrip('\n')
        data_dict["name"] = lines[1].rstrip('\n')
        data_dict["date"] = lines[2].rstrip('\n')
        data_dict["feedback"] = lines[3].rstrip('\n')
        response=requests.post(url, data=data_dict)