# -*- coding: utf-8 -*-
# @Time    : 17-9-18 上午9:58
# @Author  : shaoxin
# @Site    : 
# @File    : task
# @Software: PyCharm

import time
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')


@celery.task
def send_mail(mail):
    print('sending mail to %s...' % mail)
    time.sleep(2.0)
    print('mail sent.')




