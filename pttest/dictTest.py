# -*- coding: utf-8 -*-


from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from time import time


class ReportHandler():
    executor = ThreadPoolExecutor(20)


    @run_on_executor
    def request_process(self):
        for i in range(10):
            print i

if __name__ == "__main__":
    ReportHandler().request_process()
