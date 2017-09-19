# -*- coding: utf-8 -*-
# coding=utf-8
# import win32gui,win32api,win32con
# import time
# import threading
#
# def key():
#     interval = 0.3
#     while True:
#         time.sleep(interval)
#         win32api.keybd_event(65,0,0,0) #a键位码是86
#         win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
#         win32api.keybd_event(83,0,0,0) #s键位码是86
#         win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
#         win32api.keybd_event(68,0,0,0) #d键位码是86
#         win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
#         win32api.keybd_event(74,0,0,0) #j键位码是86
#         win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
#         win32api.keybd_event(75,0,0,0) #k键位码是86
#         win32api.keybd_event(75,0,win32con.KEYEVENTF_KEYUP,0)
#         win32api.keybd_event(76,0,0,0) #l键位码是86
#         win32api.keybd_event(76,0,win32con.KEYEVENTF_KEYUP,0)
#
# t = threading.Thread(target=key)
# t.start()f

# import numpy as np
# import pandas as pd
# from cProfile import Profile
#
# def foo():
#     return foo2()
# def foo2():
#     return foo3()
# def foo3():
#     return foo4()
# def foo4():
#     return "fafsa"
#
# def bar():
#     ret =0
#     for i in xrange(10000):
#         ret+=i*i
#     return ret
# def main():
#     ret =0
#     for i in range(10000):
#         if i%10000==0:
#             bar()
#         else:
#             foo()
#
#
# if __name__ == "__main__":
#     prof = Profile()
#     prof.runcall(main)
#     prof.print_stats()

# code for Profile

# import datetime
# a = datetime.datetime.strptime("2016-01-06","%Y-%m-%d")
#
# b = a.replace(day=1) - datetime.timedelta(1)
# print a,b
import functools
from collections import Counter

import MyQR
import numpy as np
import pandas as pd


def get_highest_frequency(place_list):
        highest_frequency_place = "未找到"
        if place_list:
            values_counts = Counter(place_list)
            highest_frequency_place = values_counts.most_common()[0][0]
        return highest_frequency_place

values=['zhangsan','lisi','lisi','wangwu','wangwu','lisi','zhangsan','zhangsan','zhangsan','zhangsan','mazi',"张三","张三","张三","张三","张三","张三","张三","张三",'mazi','wangwu','wangwu','mazi', 'lisi','mazi','mazi','mazi', 'wangwu','mazi']



print get_highest_frequency(values)
