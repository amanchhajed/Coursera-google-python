#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
from emails import *

def check_cpu_usage(cpu):
    top = psutil.cpu_percent(cpu)
    return top < 80


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free_disk = du.free / du.total * 100
    return free_disk > 20


def check_memory_usage():
    memory = psutil.virtual_memory().available
    available_memory = (memory / 1024) / 1024
    return available_memory > 500


def resolve_hostname():
    hostname = socket.gethostbyname('localhost')
    return hostname == '127.0.0.1'


def check_error():
    if not check_disk_usage('/'):
        subject = 'Error - Available disk space is less than 20%'
        return subject
    elif not check_cpu_usage(1):
        subject = 'Error - CPU usage is over 80%'
        return subject
    elif not check_memory_usage():
        subject = 'Error - Available memory is less than 500MB'
        return subject
    elif not resolve_hostname():
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        return subject
    else:
        return None


if __name__ == "__main__":
    subject = check_error()
    if subject is not None:
        body = 'Please check your system and resolve the issue as soon as possible.'
        msg = generate_email("automation@example.com", "student-02-82bcc67d0a45@example.com",
                             subject, body, None)
        send_email(msg)