# -*- coding: utf-8 -*-

import urllib2
import json


class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()

a = {"is_ok": True, "value": {"debit_card": {"name_on_card": "\u65e0\u6570\u636e", "bank_name": "\u65e0\u6570\u636e", "card_num": "\u65e0\u6570\u636e", "salary": "\u65e0\u6570\u636e", "m6_in_out": "\u65e0\u6570\u636e", "except_consume": "\u65e0\u6570\u636e", "balance": "\u65e0\u6570\u636e"}, "credit_card": {"name_on_card": "\u7530\u6d2a\u6797", "bank_name": "\u62db\u5546\u94f6\u884c", "card_num": "6225********1668", "credit_overdue": ["2017-08 \u8d26\u5355\u91d1\u989d1814.94 \u672a\u5230\u8d26\u5355\u65e5;", "2017-07 \u8d26\u5355\u91d1\u989d11199.59 \u672a\u903e\u671f;", "2017-06 \u8d26\u5355\u91d1\u989d2821.45 \u672a\u903e\u671f;", "2017-05 \u8d26\u5355\u91d1\u989d2104.67 \u672a\u903e\u671f;", "2017-04 \u8d26\u5355\u91d1\u989d1706.7 \u672a\u903e\u671f;", "2017-03 \u8d26\u5355\u91d1\u989d-541.27 \u672a\u903e\u671f;", "2017-02 \u8d26\u5355\u91d1\u989d682.03 \u672a\u903e\u671f;", "2017-01 \u8d26\u5355\u91d1\u989d11962.07 \u672a\u903e\u671f;", "2016-12 \u8d26\u5355\u91d1\u989d12190.07 \u672a\u903e\u671f;", "2016-11 \u8d26\u5355\u91d1\u989d12086.07 \u672a\u903e\u671f;", "2016-10 \u8d26\u5355\u91d1\u989d12014.92 \u672a\u903e\u671f;", "2016-09 \u8d26\u5355\u91d1\u989d11919.5 \u903e\u671f;"], "payment_date": "\u6bcf\u670804\u65e5\u8fd8\u6b3e", "cash_balance": 0.0, "new_balance": 1814.94, "except_consume": "\u65e0\u6570\u636e", "credit_limit": 20000.0, "max_consume": ["2017-08 \u6700\u5927\u6d88\u8d39\u91d1\u989d800.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u9752\u7f8a\u533a\u795e\u5947\u4e4b\u65c5\u65c5\u884c\u793e", "2017-07 \u6700\u5927\u6d88\u8d39\u91d1\u989d3082.0 \u6d88\u8d39\u5546\u5bb6 \u9f99\u6cc9\u9a7f\u533a\u67cf\u5408\u9547\u7f8e\u5bb6\u8d85\u5e02", "2017-06 \u6700\u5927\u6d88\u8d39\u91d1\u989d490.0 \u6d88\u8d39\u5546\u5bb6 \u8d26\u5355\u5206\u671f ( \u8d26\u5355 ) 05-24", "2017-05 \u6700\u5927\u6d88\u8d39\u91d1\u989d600.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u5c0f\u91d1\u7389\u9762\u5305\u5e97", "2017-04 \u6700\u5927\u6d88\u8d39\u91d1\u989d910.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u96c5\u97f5\u9152\u5e97", "2017-03 \u6700\u5927\u6d88\u8d39\u91d1\u989d800.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u5e78\u798f\u822a\u7a7a\u7968\u52a1"], "balance": 33.71, "cash_limit": 36.34}}, "description": "\u6570\u636e\u8c03\u7528\u6a21\u5757\uff1a\u4e3b\u4fe1\u7528\u5361\u8d1f\u503a-\u4e3b\u50a8\u84c4\u5361\u8d1f\u503a", "err_message": "", "err_code": 0}
b = {"is_ok": True, "value": {"debit_card": {"name_on_card": "\u65e0\u6570\u636e", "bank_name": "\u65e0\u6570\u636e", "card_num": "\u65e0\u6570\u636e", "salary": "\u65e0\u6570\u636e", "m6_in_out": "\u65e0\u6570\u636e", "except_consume": "\u65e0\u6570\u636e", "balance": "\u65e0\u6570\u636e"}, "credit_card": {"name_on_card": "\u7530\u6d2a\u6797", "bank_name": "\u62db\u5546\u94f6\u884c", "card_num": "6225********1668", "credit_overdue": ["2017-08 \u8d26\u5355\u91d1\u989d1814.94 \u672a\u5230\u8d26\u5355\u65e5;", "2017-07 \u8d26\u5355\u91d1\u989d11199.59 \u672a\u903e\u671f;", "2017-06 \u8d26\u5355\u91d1\u989d2821.45 \u672a\u903e\u671f;", "2017-05 \u8d26\u5355\u91d1\u989d2104.67 \u672a\u903e\u671f;", "2017-04 \u8d26\u5355\u91d1\u989d1706.7 \u672a\u903e\u671f;", "2017-03 \u8d26\u5355\u91d1\u989d-541.27 \u672a\u903e\u671f;", "2017-02 \u8d26\u5355\u91d1\u989d682.03 \u672a\u903e\u671f;", "2017-01 \u8d26\u5355\u91d1\u989d11962.07 \u672a\u903e\u671f;", "2016-12 \u8d26\u5355\u91d1\u989d12190.07 \u672a\u903e\u671f;", "2016-11 \u8d26\u5355\u91d1\u989d12086.07 \u672a\u903e\u671f;", "2016-10 \u8d26\u5355\u91d1\u989d12014.92 \u672a\u903e\u671f;", "2016-09 \u8d26\u5355\u91d1\u989d11919.5 \u903e\u671f;"], "payment_date": "\u6bcf\u670804\u65e5\u8fd8\u6b3e", "cash_balance": 0.0, "new_balance": 1814.94, "except_consume": "\u65e0\u6570\u636e", "credit_limit": 20000.0, "max_consume": ["2017-08 \u6700\u5927\u6d88\u8d39\u91d1\u989d800.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u9752\u7f8a\u533a\u795e\u5947\u4e4b\u65c5\u65c5\u884c\u793e", "2017-07 \u6700\u5927\u6d88\u8d39\u91d1\u989d3082.0 \u6d88\u8d39\u5546\u5bb6 \u9f99\u6cc9\u9a7f\u533a\u67cf\u5408\u9547\u7f8e\u5bb6\u8d85\u5e02", "2017-06 \u6700\u5927\u6d88\u8d39\u91d1\u989d490.0 \u6d88\u8d39\u5546\u5bb6 \u8d26\u5355\u5206\u671f ( \u8d26\u5355 ) 05-24", "2017-05 \u6700\u5927\u6d88\u8d39\u91d1\u989d600.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u5c0f\u91d1\u7389\u9762\u5305\u5e97", "2017-04 \u6700\u5927\u6d88\u8d39\u91d1\u989d910.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u96c5\u97f5\u9152\u5e97", "2017-03 \u6700\u5927\u6d88\u8d39\u91d1\u989d800.0 \u6d88\u8d39\u5546\u5bb6 \u6210\u90fd\u5e02\u5e78\u798f\u822a\u7a7a\u7968\u52a1"], "balance": 33.71, "cash_limit": 36.34}}, "description": "\u6570\u636e\u8c03\u7528\u6a21\u5757\uff1a\u4e3b\u4fe1\u7528\u5361\u8d1f\u503a-\u4e3b\u50a8\u84c4\u5361\u8d1f\u503a", "err_message": "", "err_code": 0}

print a==b