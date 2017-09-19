# -*- coding: utf-8 -*-
# @Time    : 17-9-18 上午11:37
# @Author  : shaoxin
# @Site    : 
# @File    : send
# @Software: PyCharm

from task import send_mail

if __name__ == "__main__":
    send_mail.delay('haha@mzil.org')
