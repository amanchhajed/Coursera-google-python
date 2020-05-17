#!/usr/bin/env python3
import os
import locale
import datetime
from reports import generate_report
from emails import *

description_directory = '/home/student-02-82bcc67d0a45/supplier-data/descriptions/'
description_files = os.listdir(description_directory)
def summary_string():
    ret = ""
    for description_name in description_files:
        if '.txt' in description_name:
            description_path = description_directory + description_name
            with open(description_path) as content:
                data = content.readlines()
                name = data[0].strip('\n')
                weight = int(data[1].strip('\n').strip(' lbs'))
                ret += "name: %s<br />weight: %d lbs<br/><br />"%(name, weight)  
    return ret

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on ' + str(current_date)
    new_subject = 'Upload Completed - Online Fruit Store'
    new_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    generate_report('/tmp/processed.pdf', title, summary_string())
    messagesg = generate_email("automation@example.com", "student-02-82bcc67d0a45@example.com",
                               new_subject, new_body, "/tmp/processed.pdf")
    send_email(message)
  