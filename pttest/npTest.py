# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

data_3w9 = []
data_4w5 = []
with open(r"E:\data\wanyuan.txt", 'r') as f1:
    data_3w9 = f1.readlines()
with open(r"/home/saber/Downloads/loan_no.txt", 'r') as f2:
    data_4w5 = f2.readlines()

outSet = set(data_4w5).difference(set(data_3w9))
with open(r"E:\zl.txt", 'a') as f3:
    for item in outSet:
        f3.write(item)
    print "down"


