# -*- coding: utf-8 -*-
# if __name__ =="__main__":
#     a={1:'a',2:'c',3:'d'}
#     b={1:'d',4:'es'}
#     print dict(a,**b)
#     print a
#

# if __name__ =="__main__":
#     a = 1
#     b = 2
#     c = a>b and a or b
#     print c
# import os
#
# lineList = []
# postfixes = ['.py', '.java', '.c', '.cpp', '.h']
#
# def deal_lines(file_name):
#     cmd = "dos2unix -ascii %s" %file_name
#     os.system(cmd)
#     with open(file_name, 'r') as f:
#         for line in f:
#             str = line.replace('\t', '    ').rstrip()
#             yield str + "\n"
#
# def format_covert(file_path):
#     for path, dirs, files in os.walk(file_path):
#         for name in files:
#             full_path = os.path.join(path, name)
#             norm_path = os.path.normpath(os.path.abspath(full_path))
#             modifyFileFlag = any([norm_path.endswith(postfix) for postfix in postfixes])
#             if modifyFileFlag:
#                 for line in deal_lines(norm_path):
#                     lineList.append(line)
#                 with open(norm_path, 'w+') as f:
#                     for index in range(0, len(lineList)):
#                         f.write(lineList[index])
#                 del lineList[:]

# if __name__ == '__main__':
#     file_path = os.path.join(r'G:\Credit_Report_Server_new','')
#     format_covert(file_path)
from functools import wraps
from time import time


# def fn_timer(function):
#     @wraps(function)
#     def function_timer(*args, **kwargs):
#         t0 = time()
#         result = function(*args, **kwargs)
#         t1 = time()
#         print ("Total time running %s: %s seconds" %
#                (function.func_name, str(t1-t0))
#                )
#         return result
#     return function_timer
#
# @fn_timer
# def foo1(a):
#     return map(lambda x:x**2,a)
#
# @fn_timer
# def foo2(a):
#     b=[]
#     for i in a:
#         b.append(i**2)
#     return b
#
# def fbin():
#     fibs=[0,1]
#     num =input('How many Fibonacci do you want?')
#     for i in range(num-2):
#         fibs.append(fibs[-2]+fibs[-1])
#     print(fibs)
#
# def zs():
#     a = ""
#

# class Test(object):
#     v1 ='va1'
#     count = 0
#
#     def __init__(self):
#         self.v2='va2'
#
#     @classmethod
#     def cls_med(cls):
#         print cls.v1
#         cls.v1='dfaffa'
#         cls.count+=1
#         print cls.count
#
#     def get_v2(self):
#         print self.v2
#     def set_v2(self,value):
#         self.v2 = value
#     @staticmethod
#     def stc_med():
#         pass
#
# if __name__ == '__main__':
#     t1 = Test()
#     t2 = Test()
#     t1.set_v2('afa')
#     t1.get_v2()
#     t2.get_v2()
#     t2.set_v2('brvd')
#     t1.get_v2()
#     Test().cls_med()
#     t1.cls_med()
#     t2.cls_med()

# import re
# def fuzzyfinder(user_input, collection):
#     suggestions = []
#     pattern = '.*？'.join(user_input) # Converts 'djm' to 'd.*j.*m'
#     regex = re.compile(pattern)     # Compiles a regex.
#     for item in collection:
#         match = regex.search(item)  # Checks if the current item matches the regex.
#         if match:
#             suggestions.append((len(match.group()), match.start(), item))
#     return [x[-1] for x in sorted(suggestions)]
#
#
#
#
# if __name__ == '__main__':
#     collection = ['django_migrations.py',
#                 'django_admin_log.py',
#                 'main_generator.py',
#                 'migrations.py',
#                 'api_user.doc',
#                 'user_group.doc',
#                 'accounts.txt',
#                 ]
#
#     print fuzzyfinder('mig', collection)

# def foo(data):
#     print data
#
# if __name__ == '__main__':
#     data = "print"
#     foo(data)


def foo():
    return [lambda x: i * x for i in range(5)]


def gen_example():
    print 1
    yield 2
    print 3
    yield 4
    print 5


def fib():
    a, b = 1, 1
    while a < 10:
        yield a
        a, b = b, a + b
        # print a, b
class helf:
    def __init__(self):
        self.other_person_contact_map={'noon_contact_time': -999, 'parents_callout_cnt_2m': -999, 'workday_contact_cnt': -999, 'contact_person_in_phonedetail_rate': -999, 'contact_person_in_phonedetail_cnt': -999, 'parents_callout_cnt_1m': -999, 'time_per_cnt': -999, 'parents_contact_time_1m': -999, 'max_parents_silence_days': -999, 'cnt_per_address': -999, 'contact_mutual_cnt': -999, 'total_contact_time': -999, 'receiver_parents_cnt': -999, 'if_parents_contact_2m': -999, 'holiday_contact_cnt': -999, 'receiver_cnt': -999, 'if_parents_in_detail_info': -999, 'others_use_parents_title_contact_time': 0, 'if_parents_in_receiver': 1, 'if_parents_in_addressbook': -999, 'max_parents_silence_days_2m': -999, 'noon_contact_cnt': -999, 'max_parents_silence_days_1m': -999, 'parents_mutual_cnt': -999, 'total_call_type': -999, 'parents_callout_time_1m': -999, 'parents_contact_cnt_1m': -999, 'amount_per_cnt': 1.0, 'contact_person_in_addressbook_cnt': -999, 'if_parents_in_any': 0, 'parents_mutual_cnt_1m': -999, 'morning_contact_time': -999, 'time_per_day': -999, 'if_contact_person_in_any': 1, 'contact_person_in_intimates_rate': 1.0, 'cnt_per_day': -999, 'parents_contact_cnt_2m': -999, 'if_parents_contact_1m': -999, 'contact_person_in_intimates_cnt': 1, 'early_moring_contact_time': -999, 'cnt_per_mon': -999, 'total_contact_cnt': -999, 'total_contact_address': -999, 'night_contact_cnt': -999, 'total_init_type': -999, 'workday_contact_time': -999, 'parents_contact_time_2m': -999, 'if_contact_person_in_intimates': 1, 'contact_period_days': -999, 'contact_person_cnt': 1, 'contact_person_in_addressbook_rate': -999, 'if_parents_in_intimates': -999, 'afternoon_contact_cnt': -999, 'if_others_use_parents_title': 0, 'total_contact_days': -999, 'amount_per_address': -999, 'recently_contact_days': -999, 'parents_callout_time_over2m': -999, 'morning_contact_cnt': -999, 'time_per_mon': -999, 'parents_callout_time_2m': -999, 'receiver_parents_amount': -999, 'afternoon_contact_time': -999, 'parents_callout_cnt_over2m': -999, 'holiday_contact_time': -999, 'others_use_parents_title_cnt': 0, 'weekend_contact_cnt': -999, 'early_moring_contact_cnt': -999, 'weekend_contact_time': -999, 'night_contact_time': -999, 'total_contact_mons': -999, 'if_parents_title_in_addressbook': 0, 'total_parents_receiver_address_cnt': 1, 'others_use_parents_title_contact_cnt': 0, 'parents_mutual_cnt_2m': -999}

    def k22(self):
        k22 = {
                "total_contact_cnt": str(
                        self.other_person_contact_map["total_contact_cnt"]),
                "total_contact_time": str(
                        self.other_person_contact_map["total_contact_time"]),
                "time_per_cnt": str(
                        self.other_person_contact_map["time_per_cnt"]),
                "contact_person_cnt": str(
                        self.other_person_contact_map["contact_person_cnt"]),
                "contact_person_in_addressbook_cnt": str(
                        self.other_person_contact_map[
                            "contact_person_in_addressbook_cnt"]),
                "contact_person_in_addressbook_rate": str(
                        self.other_person_contact_map[
                            "contact_person_in_addressbook_rate"]),
                "contact_person_in_phonedetail_cnt": str(
                        self.other_person_contact_map[
                            "contact_person_in_phonedetail_cnt"]),
                "contact_person_in_phonedetail_rate": str(
                        self.other_person_contact_map[
                            "contact_person_in_phonedetail_rate"]),
                "if_contact_person_in_any": str(self.other_person_contact_map[
                                                    "if_contact_person_in_any"]),
                "if_contact_person_in_intimates": str(
                        self.other_person_contact_map[
                            "if_contact_person_in_intimates"]),
                "contact_person_in_intimates_cnt": str(
                        self.other_person_contact_map[
                            "contact_person_in_intimates_cnt"]),
                "contact_person_in_intimates_rate": str(
                        self.other_person_contact_map[
                            "contact_person_in_intimates_rate"]),
                "contact_mutual_cnt": str(
                        self.other_person_contact_map["contact_mutual_cnt"]),
                "receiver_parents_cnt": str(
                        self.other_person_contact_map[
                            "receiver_parents_cnt"]),
                "receiver_parents_amount": str(
                        self.other_person_contact_map[
                            "receiver_parents_amount"]),
                "amount_per_cnt": str(
                        self.other_person_contact_map["amount_per_cnt"]),
                "total_parents_receiver_address_cnt": str(
                        self.other_person_contact_map["total_parents_receiver_address_cnt"]),
                "cnt_per_address": str(
                        self.other_person_contact_map["cnt_per_address"]),
                "amount_per_address": str(
                        self.other_person_contact_map["amount_per_address"]),
                "contact_person_in_receiver": str(
                        self.other_person_contact_map["contact_person_in_receiver"]),
                "receiver_cnt": str(
                        self.other_person_contact_map["receiver_cnt"]),
                "parents_contact_cnt_1m": str(
                        self.parents_contact_map["parents_contact_cnt_1m"]),
                "parents_contact_cnt_2m": str(
                        self.parents_contact_map["parents_contact_cnt_2m"]),
                "parents_contact_time_1m": str(
                        self.parents_contact_map["parents_contact_time_1m"]),
                "parents_contact_time_2m": str(
                        self.parents_contact_map["parents_contact_time_2m"]),
                "if_parents_contact_1m": str(
                        self.parents_contact_map["if_parents_contact_1m"]),
                "if_parents_contact_2m": str(
                        self.parents_contact_map["if_parents_contact_2m"]),
                "parents_callout_cnt_1m": str(
                        self.parents_contact_map["parents_callout_cnt_1m"]),
                "parents_callout_cnt_2m": str(
                        self.parents_contact_map["parents_callout_cnt_2m"]),
                "parents_callout_time_1m": str(
                        self.parents_contact_map["parents_callout_time_1m"]),
                "parents_callout_time_2m": str(
                        self.parents_contact_map["parents_callout_time_2m"]),
                "parents_callout_cnt_over2m": str(
                        self.parents_contact_map["parents_callout_cnt_over2m"]),
                "parents_callout_time_over2m": str(self.parents_contact_map[
                                                       "parents_callout_time_over2m"]),
                "parents_mutual_cnt_1m": str(
                        self.parents_contact_map["parents_mutual_cnt_1m"]),
                "parents_mutual_cnt_2m": str(
                        self.parents_contact_map["parents_mutual_cnt_2m"]),
                "max_parents_silence_days": str(
                        self.parents_contact_map["max_parents_silence_days"]),
                "max_parents_silence_days_1m": str(self.parents_contact_map[
                                                       "max_parents_silence_days_1m"]),
                "max_parents_silence_days_2m": str(self.parents_contact_map[
                                                       "max_parents_silence_days_2m"]),
                "contact_period_days": str(
                        self.other_person_contact_map["contact_period_days"]),
                "recently_contact_days": str(
                        self.other_person_contact_map["recently_contact_days"]),
                "total_contact_days": str(
                        self.other_person_contact_map["total_contact_days"]),
                "cnt_per_day": str(
                        self.other_person_contact_map["cnt_per_day"]),
                "time_per_day": str(
                        self.other_person_contact_map["time_per_day"]),
                "total_contact_mons": str(
                        self.other_person_contact_map["total_contact_mons"]),
                "cnt_per_mon": str(
                        self.other_person_contact_map["cnt_per_mon"]),
                "time_per_mon": str(
                        self.other_person_contact_map["time_per_mon"]),
                "total_contact_address": str(
                        self.other_person_contact_map["total_contact_address"]),
                "total_init_type": str(
                        self.other_person_contact_map["total_init_type"]),
                "total_call_type": str(
                        self.other_person_contact_map["total_call_type"]),
                "morning_contact_cnt": str(
                        self.other_person_contact_map["morning_contact_cnt"]),
                "morning_contact_time": str(
                        self.other_person_contact_map["morning_contact_time"]),
                "noon_contact_cnt": str(
                        self.other_person_contact_map["noon_contact_cnt"]),
                "noon_contact_time": str(
                        self.other_person_contact_map["noon_contact_time"]),
                "afternoon_contact_cnt": str(
                        self.other_person_contact_map["afternoon_contact_cnt"]),
                "afternoon_contact_time": str(self.other_person_contact_map[
                                                  "afternoon_contact_time"]),
                "night_contact_cnt": str(
                        self.other_person_contact_map["night_contact_cnt"]),
                "night_contact_time": str(
                        self.other_person_contact_map["night_contact_time"]),
                "early_moring_contact_cnt": str(self.other_person_contact_map[
                                                    "early_moring_contact_cnt"]),
                "early_moring_contact_time": str(self.other_person_contact_map[
                                                     "early_moring_contact_time"]),
                "workday_contact_cnt": str(
                        self.other_person_contact_map["workday_contact_cnt"]),
                "workday_contact_time": str(
                        self.other_person_contact_map["workday_contact_time"]),
                "weekend_contact_cnt": str(
                        self.other_person_contact_map["weekend_contact_cnt"]),
                "weekend_contact_time": str(
                        self.other_person_contact_map["weekend_contact_time"]),
                "holiday_contact_cnt": str(
                        self.other_person_contact_map["holiday_contact_cnt"]),
                "holiday_contact_time": str(
                        self.other_person_contact_map["holiday_contact_time"])
                # "create_time": datetime.now()
            }
        k2 = {'noon_contact_time': -999, 'parents_callout_cnt_2m': -999, 'workday_contact_cnt': -999, 'contact_person_in_phonedetail_rate': -999, 'contact_person_in_phonedetail_cnt': -999, 'parents_callout_cnt_1m': -999, 'time_per_cnt': -999, 'parents_contact_time_1m': -999, 'max_parents_silence_days': -999, 'cnt_per_address': -999, 'contact_mutual_cnt': -999, 'total_contact_time': -999, 'receiver_parents_cnt': -999, 'if_parents_contact_2m': -999, 'holiday_contact_cnt': -999, 'receiver_cnt': -999, 'if_parents_in_detail_info': -999, 'others_use_parents_title_contact_time': 0, 'if_parents_in_receiver': 1, 'if_parents_in_addressbook': -999, 'max_parents_silence_days_2m': -999, 'noon_contact_cnt': -999, 'max_parents_silence_days_1m': -999, 'parents_mutual_cnt': -999, 'total_call_type': -999, 'parents_callout_time_1m': -999, 'parents_contact_cnt_1m': -999, 'amount_per_cnt': 1.0, 'contact_person_in_addressbook_cnt': -999, 'if_parents_in_any': 0, 'parents_mutual_cnt_1m': -999, 'morning_contact_time': -999, 'time_per_day': -999, 'if_contact_person_in_any': 1, 'contact_person_in_intimates_rate': 1.0, 'cnt_per_day': -999, 'parents_contact_cnt_2m': -999, 'if_parents_contact_1m': -999, 'contact_person_in_intimates_cnt': 1, 'early_moring_contact_time': -999, 'cnt_per_mon': -999, 'total_contact_cnt': -999, 'total_contact_address': -999, 'night_contact_cnt': -999, 'total_init_type': -999, 'workday_contact_time': -999, 'parents_contact_time_2m': -999, 'if_contact_person_in_intimates': 1, 'contact_period_days': -999, 'contact_person_cnt': 1, 'contact_person_in_addressbook_rate': -999, 'if_parents_in_intimates': -999, 'afternoon_contact_cnt': -999, 'if_others_use_parents_title': 0, 'total_contact_days': -999, 'amount_per_address': -999, 'recently_contact_days': -999, 'parents_callout_time_over2m': -999, 'morning_contact_cnt': -999, 'time_per_mon': -999, 'parents_callout_time_2m': -999, 'receiver_parents_amount': -999, 'afternoon_contact_time': -999, 'parents_callout_cnt_over2m': -999, 'holiday_contact_time': -999, 'others_use_parents_title_cnt': 0, 'weekend_contact_cnt': -999, 'early_moring_contact_cnt': -999, 'weekend_contact_time': -999, 'night_contact_time': -999, 'total_contact_mons': -999, 'if_parents_title_in_addressbook': 0, 'total_parents_receiver_address_cnt': 1, 'others_use_parents_title_contact_cnt': 0, 'parents_mutual_cnt_2m': -999}
        for key in k22:
            if key not in k2:
                print key

if __name__ == "__main__":
    helf().k22()

# if __name__ == "__main__":
#     import numpy as np
#     import pandas as pd
#     dates = pd.DataFrame(np.random.randn(6,4),index= [1,2,3,4,5,6],columns=list('abcd'))
#     t = dates["a"]
#     b = t.map(lambda x:x)
#     print type(t)
#     print b
#     k1 = {'noon_contact_time': 2587L, 'parents_callout_cnt_2m': 160, 'workday_contact_cnt': 639, 'contact_person_in_phonedetail_rate': -999, 'contact_person_in_phonedetail_cnt': -999, 'parents_callout_cnt_1m': 62, 'time_per_cnt': 45.56, 'parents_contact_time_1m': 4216, 'max_parents_silence_days': 2, 'cnt_per_address': -999, 'contact_mutual_cnt': -999, 'total_contact_time': 39136, 'receiver_parents_cnt': -999, 'if_parents_contact_2m': 1, 'holiday_contact_cnt': 0, 'receiver_cnt': -999, 'if_parents_in_detail_info': 1, 'parents_contact_cnt_2m': 330, 'if_parents_in_receiver': -999, 'if_parents_in_addressbook': -999, 'max_parents_silence_days_2m': 1, 'noon_contact_cnt': 73, 'max_parents_silence_days_1m': 1, 'parents_mutual_cnt': 405, 'total_call_type': 3, 'parents_callout_time_1m': 2253, 'parents_contact_cnt_1m': 144, 'amount_per_cnt': -999, 'contact_person_in_addressbook_cnt': -999, 'if_parents_in_any': 1, 'parents_mutual_cnt_1m': 62, 'morning_contact_time': 10683L, 'time_per_day': 243.08, 'if_contact_person_in_any': -999, 'contact_person_in_intimates_rate': -999, 'cnt_per_day': 5.34, 'others_use_parents_title_contact_time': 0, 'if_parents_contact_1m': 1, 'contact_person_in_intimates_cnt': -999, 'early_moring_contact_time': 475L, 'cnt_per_mon': 143.17, 'total_contact_cnt': 859, 'total_contact_address': 3, 'night_contact_cnt': 170, 'total_init_type': 2, 'workday_contact_time': 26876L, 'parents_contact_time_2m': 11533, 'if_contact_person_in_intimates': -999, 'contact_period_days': 166L, 'contact_person_cnt': -999, 'contact_person_in_addressbook_rate': -999, 'if_parents_in_intimates': 0, 'afternoon_contact_cnt': 332, 'if_others_use_parents_title': 0, 'total_contact_days': 161, 'amount_per_address': -999, 'recently_contact_days': 0L, 'parents_callout_time_over2m': 10804, 'morning_contact_cnt': 274, 'time_per_mon': 6522.67, 'parents_callout_time_2m': 6504, 'receiver_parents_amount': -999, 'afternoon_contact_time': 13993L, 'parents_callout_cnt_over2m': 238, 'holiday_contact_time': 0, 'others_use_parents_title_cnt': 0, 'weekend_contact_cnt': 220, 'early_moring_contact_cnt': 10, 'weekend_contact_time': 12260L, 'night_contact_time': 11398L, 'total_contact_mons': 6, 'if_parents_title_in_addressbook': 0, 'total_parents_receiver_address_cnt': -999, 'others_use_parents_title_contact_cnt': 0, 'parents_mutual_cnt_2m': 160}
#     k2 = {'noon_contact_time': 0, 'parents_callout_cnt_2m': 160, 'workday_contact_cnt': 26, 'contact_person_in_phonedetail_rate': 1.0, 'contact_person_in_phonedetail_cnt': 1, 'parents_callout_cnt_1m': 62, 'time_per_cnt': 10014.86, 'parents_contact_time_1m': 4216, 'max_parents_silence_days': 25, 'cnt_per_address': -999, 'contact_mutual_cnt': set([u'17191385555', u'18137053555', u'13592319875', u'03706011376', u'15517037188', u'13781523111', u'13700837158', u'13613708196', u'13938931265', u'03706581004', u'03703136988', u'13592317088', u'18738077000', u'15837018185', u'15896959166', u'13937099888', u'13937079316', u'13087025671', u'03703032100', u'15836417444', u'18237041444', u'13937079258', u'13903701705', u'18537049888', u'13592386717', u'18749505888', u'15518765289', u'15544436999', u'03703032109', u'13700831989', u'15939081629', u'13837062138', u'13462721888', u'15837011888', u'15839037553', u'13837053785', u'03702636211', u'03708222280', u'15090688835', u'13460122273', u'03706018339', u'13849648288', u'15565029287', u'15037021666', u'13849688380', u'03703788836', u'055164382743', u'15090552899', u'15637043333', u'13703977950', u'13526309899', u'18637031885', u'13569368186', u'03703032178', u'15514949565', u'03705094006', u'13921662064', u'15162570975', u'13849665271', u'13526315855', u'15137083003', u'13849685299', u'03702788260', u'15082966880', u'13523158705', u'15729210026', u'15985046772', u'18237016668', u'15539054555', u'15993448188', u'03706733770', u'18338722207', u'03703032169', u'18236373599', u'15090633893', u'17737056782', u'03703338885', u'13523806333', u'13781617867', u'15560063899', u'15836493158', u'18603707555', u'13781682606', u'13569358777', u'15036696996', u'15518729111', u'15037065226', u'15518600959', u'15136059239', u'15082912345', u'13598350951', u'18937017763', u'13598374468', u'13460195908', u'15303703999', u'18601355341', u'03706699222', u'15937085877', u'13103330350', u'15637008602', u'13569395386', u'13569333315', u'15672867999', u'13921666691', u'13462791588', u'15238500515', u'15993961666', u'15003702986', u'18637083886', u'15939057299', u'03706961608', u'13598351958', u'18530276778', u'15837018668', u'15713620042', u'15137012678', u'13592317915', u'15237070138', u'13937091035', u'15729479333', u'03703035161', u'13271083266', u'13592334617', u'15003705523', u'13781529888', u'13937051111', u'15937073045', u'15937036600', u'13949931666', u'18438308888', u'03703932225', u'13592361117', u'4000012222', u'03706689699', u'18339265989', u'15938387649', u'15517076688', u'15517037779', u'13703977611', u'13703428058', u'18137012759', u'18637034041', u'13937038683', u'18438301234', u'13592378666', u'075536356766', u'03703032034', u'13598395666', u'13781563283', u'13643708368', u'15560050790', u'15082910588', u'15895605134', u'15617016777', u'15824770199', u'15090600555', u'15938322711', u'18537082789', u'13700704667', u'15503874999', u'03702782105', u'13700837567', u'15560053865']), 'total_contact_time': 290431, 'receiver_parents_cnt': -999, 'if_parents_contact_2m': 1, 'holiday_contact_cnt': 0, 'receiver_cnt': -999, 'if_parents_in_detail_info': 1, 'parents_contact_cnt_2m': 330, 'if_parents_in_receiver': -999, 'if_parents_in_addressbook': -999, 'max_parents_silence_days_2m': -999, 'noon_contact_cnt': 0, 'max_parents_silence_days_1m': -999, 'parents_mutual_cnt': 405, 'total_call_type': 1, 'parents_callout_time_1m': 2253, 'parents_contact_cnt_1m': 144, 'amount_per_cnt': -999, 'contact_person_in_addressbook_cnt': -999, 'if_parents_in_any': 1, 'parents_mutual_cnt_1m': 62, 'morning_contact_time': 460L, 'time_per_day': 18151.94, 'if_contact_person_in_any': -999, 'contact_person_in_intimates_rate': -999, 'cnt_per_day': 1.81, 'others_use_parents_title_contact_time': 0, 'if_parents_contact_1m': 1, 'contact_person_in_intimates_cnt': -999, 'early_moring_contact_time': 0, 'cnt_per_mon': 9.67, 'total_contact_cnt': 29, 'total_contact_address': 1, 'night_contact_cnt': 0, 'total_init_type': 2, 'workday_contact_time': 1564L, 'parents_contact_time_2m': 11533, 'if_contact_person_in_intimates': -999, 'contact_period_days': 74L, 'contact_person_cnt': 1, 'contact_person_in_addressbook_rate': -999, 'if_parents_in_intimates': 0, 'afternoon_contact_cnt': 19, 'if_others_use_parents_title': 0, 'total_contact_days': 16, 'amount_per_address': -999, 'recently_contact_days': -87L, 'parents_callout_time_over2m': 10804, 'morning_contact_cnt': 10, 'time_per_mon': 96810.33, 'parents_callout_time_2m': 6504, 'receiver_parents_amount': -999, 'afternoon_contact_time': 1284L, 'parents_callout_cnt_over2m': 238, 'holiday_contact_time': 0, 'others_use_parents_title_cnt': 0, 'weekend_contact_cnt': 3, 'early_moring_contact_cnt': 0, 'weekend_contact_time': 180L, 'night_contact_time': 0, 'total_contact_mons': 3, 'if_parents_title_in_addressbook': 0, 'total_parents_receiver_address_cnt': -999, 'others_use_parents_title_contact_cnt': 0, 'parents_mutual_cnt_2m': 160}
#     k3 = parents_contact_map = {
#     "total_contact_cnt": -999,
#     "total_contact_time": -999,
#     "time_per_cnt": -999,
#     "if_parents_in_addressbook": -999,
#     "if_parents_in_detail_info": -999,
#     "if_parents_in_any": -999,
#     "if_parents_in_intimates": -999,
#     "if_contact_person_in_any":-999,
#     "if_contact_person_in_intimates":-999,
#     "contact_person_in_intimates_cnt":-999,
#     "contact_person_in_intimates_rate":-999,
#     "contact_mutual_cnt":-999,
#     "contact_person_cnt":-999,
#     "contact_person_in_addressbook_cnt":-999,
#     "contact_person_in_addressbook_rate":-999,
#     "contact_person_in_phonedetail_cnt":-999,
#     "contact_person_in_phonedetail_rate":-999,
#     "parents_mutual_cnt": -999,
#     "receiver_cnt": -999,
#     "if_parents_title_in_addressbook": -999,
#     "receiver_parents_cnt": -999,
#     "receiver_parents_amount": -999,
#     "amount_per_cnt": -999,
#     "total_parents_receiver_address_cnt": -999,
#     "cnt_per_address": -999,
#     "amount_per_address": -999,
#     "if_parents_in_receiver": -999,
#     "parents_contact_cnt_1m": -999,
#     "parents_contact_cnt_2m": -999,
#     "parents_contact_time_1m": -999,
#     "parents_contact_time_2m": -999,
#     "if_parents_contact_1m": -999,
#     "if_parents_contact_2m": -999,
#     "parents_callout_cnt_1m": -999,
#     "parents_callout_cnt_2m": -999,
#     "parents_callout_time_1m": -999,
#     "parents_callout_time_2m": -999,
#     "parents_callout_cnt_over2m": -999,
#     "parents_callout_time_over2m": -999,
#     "parents_mutual_cnt_1m": -999,
#     "parents_mutual_cnt_2m": -999,
#     "max_parents_silence_days": -999,
#     "max_parents_silence_days_1m": -999,
#     "max_parents_silence_days_2m": -999,
#     "contact_period_days": -999,
#     "recently_contact_days": -999,
#     "total_contact_days": -999,
#     "cnt_per_day": -999,
#     "time_per_day": -999,
#     "total_contact_mons": -999,
#     "cnt_per_mon": -999,
#     "time_per_mon": -999,
#     "total_contact_address": -999,
#     "total_init_type": -999,
#     "total_call_type": -999,
#     "morning_contact_cnt": -999,
#     "morning_contact_time": -999,
#     "noon_contact_cnt": -999,
#     "noon_contact_time": -999,
#     "afternoon_contact_cnt": -999,
#     "afternoon_contact_time": -999,
#     "night_contact_cnt": -999,
#     "night_contact_time": -999,
#     "early_moring_contact_cnt": -999,
#     "early_moring_contact_time": -999,
#     "workday_contact_cnt": -999,
#     "workday_contact_time": -999,
#     "weekend_contact_cnt": -999,
#     "weekend_contact_time": -999,
#     "holiday_contact_cnt": -999,
#     "holiday_contact_time": -999,
#     "others_use_parents_title_contact_time":-999,
#     "if_others_use_parents_title":-999,
#     "others_use_parents_title_cnt":-999,
#     "others_use_parents_title_contact_cnt":-999
# }
#
#
#     for item in k1:
#         if item not in k3:
#             print item
#     print "-----------------"
#     for item in k2:
#         if item not in k3:
#             print item
#
#
#
#     # from business_calendar import Calendar
#     # from datetime import datetime
#     # d1 = datetime.strptime("2030-12-25 14:00:00", "%Y-%m-%d %H:%M:%S")
#     # cal = Calendar()
#     # print cal.isholiday(d1)
#
