# -*- coding: utf-8 -*-
import datetime as dt
import pandas as pd
from utils.constants import zs_shop_map_ful
from utils.db import DBConn


class ShopHandler:
    def __init__(self):
        self.db = DBConn('it_online')
        self.it_db = DBConn('edw')
        self.iit_db = DBConn('it')
        self.shop_map_ful = zs_shop_map_ful

    def get_month_repay_amt(self, user_id):
        # 设置月还款金额
        month_repay_amt = 200
        pro_sql = "select mth_repay_amt from b_lo_loan_info where cust_no = '%s' " % user_id
        pro_data = self.iit_db.execute(pro_sql)
        if pro_data and str.isdigit(pro_data[0][0]):
            month_repay_amt = int(pro_data[0][0])
        return month_repay_amt

    def check_shop_account_ful(self, user_id):
        shop_sql = "select user_id,case when web_site='淘宝' " \
                   "then 'tb' else 'jd' end web_site," \
                   "case when is_identity='是' then 1 else 0 end is_identity, email " \
                   "from zs_shop_jd_tb_info " \
                   "where user_id='%s' " % user_id
        shop_info = self.db.execute(shop_sql)
        # print 'shop_info: %s' % user_id
        # print shop_info
        if shop_info:
            for cell in shop_info:
                if cell[1] == "tb":
                    #有淘宝账号
                    self.shop_map_ful["has_tb_account"] = 1
                    #淘宝账号实名认证
                    self.shop_map_ful["tb_is_identity"] = cell[2]
                elif cell[1] == "jd":
                    #京东账号
                    self.shop_map_ful["has_jd_account"] = 1
                    #京东账号已实名认证
                    self.shop_map_ful["jd_is_identity"] = cell[2]
                # email
                if cell[3]:
                    #使用QQ邮箱
                    self.shop_map_ful['is_use_qqmail'] = 1 if cell[3].find('qq.com')>=0 else 0
                    #使用vip QQ邮箱
                    self.shop_map_ful['is_use_vip_qqmail'] = 1 if cell[3].find('vip.qq.com')>=0 else 0
                    # 只对明确的邮箱进行处理
                    if (self.shop_map_ful['is_use_qqmail'] == 1 or self.shop_map_ful['is_use_vip_qqmail'] == 1) and cell[3].find('@') >= 0:
                        email=cell[3].encode('utf-8')
                        email_split=email.split('@')
                        if str.isdigit(email_split[0].replace('*','').strip()):
                            #qq号长度
                            self.shop_map_ful['length_qq'] = len(email_split[0])
                            #QQ邮箱是否使用昵称
                            self.shop_map_ful['is_use_nickname_qqmail'] = 0
                        else:
                            self.shop_map_ful['is_use_nickname_qqmail'] = 1

    def set_blank_note_ful(self, user_id):
        if self.shop_map_ful["has_jd_account"]:
            shop_sql = "select user_id,blank_n_note,credit_wait_pay,credit_limit from zs_shop_blank_note where user_id='%s' ORDER BY id desc limit 1 " % user_id
            shop_info = self.db.execute(shop_sql)
            if shop_info:
                #白条授信额度
                self.shop_map_ful["blank_note"] = round(shop_info[0][1],2)
                #白条可用额度
                self.shop_map_ful["blank_note_balance"] = round(shop_info[0][3],2)
                #是否使用过白条
                self.shop_map_ful['is_use_blanknote'] = 1 if shop_info[0][2]>0 else 0
                #白条已使用额度
                self.shop_map_ful['use_blanknote_amount'] = round(shop_info[0][2],2)
                #使用比例
                if self.shop_map_ful["blank_note"] > 0:
                    self.shop_map_ful['use_blanknote_rate'] = round(float(shop_info[0][2]) / float(shop_info[0][1]),2)

    def check_address_info_ful(self, user_id):
        if self.shop_map_ful["has_tb_account"] == 1 or self.shop_map_ful["has_jd_account"] == 1:
            date_sql = "select create_time from zs_shop_deliver_address where user_id='%s' order by id desc limit 1" % user_id
            date_time = self.db.execute(date_sql)
            if date_time:
                date_time = str(date_time[0][0])
                user_sql = "select user_id,begin_date,end_date,total_amount,total_count,address from zs_shop_deliver_address where user_id='%s' and create_time='%s' " % (user_id, date_time)
                user_info = self.db.execute(user_sql)
                count_list = list()
                amount_list = list()
                one_time_list = list()
                days_list = list()
                addr_list = list()
                end_date_list = list()
                for cell in user_info:
                    count_list.append(cell[4])
                    amount_list.append(cell[3])
                    addr_list.append(cell[5])
                    end_date_list.append(cell[2])
                    if cell[4] == 1:
                        one_time_list.append(cell[4])
                    if cell[1] and cell[2]:
                        a_ = dt.datetime.strptime(str(cell[1]), '%Y-%m-%d %H:%M:%S')
                        b_ = dt.datetime.strptime(str(cell[2]), '%Y-%m-%d %H:%M:%S')
                        c = b_ - a_
                        days_list.append(c.days)
                if count_list:
                    #地址对应最大消费次
                    self.shop_map_ful["max_address_cnt"] = max(count_list)
                    #地址对应最小消费次数
                    self.shop_map_ful["min_address_cnt"] = min(count_list)
                    #地址对应最大消费金额
                    self.shop_map_ful["max_address_amount"] = round(max(amount_list),2)
                    #地址对应最小消费金额
                    self.shop_map_ful["min_address_amount"] = round(min(amount_list),2)
                    #地址对应消费次数总和
                    self.shop_map_ful["total_address_cnt"] = sum(count_list)
                if one_time_list:
                    #只消费过一次的地址个数
                    self.shop_map_ful["shop_one_address_cnt"] = len(one_time_list)
                if days_list:
                    #地址消费最大间隔时间
                    self.shop_map_ful["max_address_between_days"] = max(days_list)
                    #地址消费最小间隔时间
                    self.shop_map_ful["min_address_between_days"] = min(days_list)
                if addr_list:
                    #地址总数
                    self.shop_map_ful['sum_addresses'] = len(set(addr_list))
                if end_date_list:
                    latest_date = str(max(end_date_list))
                    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d %H:%M:%S')
                    time_now = dt.datetime.now()
                    #最近一次购物距离现在的天数
                    self.shop_map_ful['recently_shop_days'] = (time_now - latest_date).days

    def check_mon_info_ful(self, user_id):

        if self.shop_map_ful["has_tb_account"] == 1 and self.shop_map_ful["has_jd_account"] == 1:
            tb_sql = "select create_time from zs_shop_expense where user_id = '%s' " \
                     "and web_site='淘宝' order by id desc limit 1" % user_id
            tb_date = self.db.execute(tb_sql)
            if tb_date:
                date_time = str(tb_date[0][0])
                tb_sql = "select user_id,web_site,`month`,count,change_address_count," \
                         "expense from zs_shop_expense " \
                         "where user_id = '%s' and web_site='淘宝' " \
                         "and create_time='%s' ORDER BY `month` desc " % (user_id, date_time)
                tb_info = self.db.execute(tb_sql)
                if tb_info:
                    tb_cnt_list = list()
                    tb_amount_list = list()
                    tb_address_change_list = list()
                    tb_month_list = list()
                    for cell in tb_info:
                        tb_cnt_list.append(cell[3])
                        tb_amount_list.append(cell[5])
                        tb_address_change_list.append(cell[4])
                        tb_month_list.append(cell[2])

            jd_sql = "select create_time from zs_shop_expense where user_id = '%s' " \
                     "and web_site='京东' order by id desc limit 1" % user_id
            jd_date = self.db.execute(tb_sql)
            if jd_date:
                date_time = str(jd_date[0][0])
                jd_sql = "select user_id,web_site,`month`,count,change_address_count," \
                         "expense from zs_shop_expense " \
                         "where user_id = '%s' and web_site='京东' " \
                         "and create_time='%s' ORDER BY `month` desc " % (user_id, date_time)
                jd_info = self.db.execute(jd_sql)
                if jd_info:
                    #self.shop_map_ful["recently_mon_cnt"] = jd_info[0][3]
                    #self.shop_map_ful["recently_mon_amount"] = round(jd_info[0][5],2)
                    jd_cnt_list = list()
                    jd_amount_list = list()
                    jd_address_change_list = list()
                    jd_month_list = list()
                    for cell in jd_info:
                        jd_cnt_list.append(cell[3])
                        jd_amount_list.append(cell[5])
                        jd_address_change_list.append(cell[4])
                        jd_month_list.append(cell[2])
            if tb_date and jd_date and tb_info and jd_info:
                #最近月消费次数
                self.shop_map_ful["recently_mon_cnt"] = min(tb_info[0][3], jd_info[0][3])
                #最近月消费月的金额
                self.shop_map_ful["recently_mon_amount"] = round(min(tb_info[0][5], jd_info[0][5]),2)
                #最大消费月份次数
                self.shop_map_ful["max_mon_cnt"] = max(max(tb_cnt_list), max(jd_cnt_list))
                #最小消费月次数
                self.shop_map_ful["min_mon_cnt"] = min(min(tb_cnt_list), min(jd_cnt_list))
                #最大消费月份金额
                self.shop_map_ful["max_mon_amount"] =round(max(max(tb_amount_list), max(jd_amount_list)),2)
                #最小消费月份金额
                self.shop_map_ful["min_mon_amount"] = round(min(min(tb_amount_list), min(jd_amount_list)),2)
                #总消费次数
                self.shop_map_ful["total_shop_cnt"] = sum(tb_cnt_list) + sum(jd_cnt_list)
                #总消费金额
                self.shop_map_ful["total_shop_amount"] = round(sum(tb_amount_list) + sum(jd_amount_list),2)
                #淘宝消费次数
                self.shop_map_ful["tb_shop_cnt"] = sum(tb_cnt_list)
                #淘宝消费金额
                self.shop_map_ful["tb_expense_amount"] = round(sum(tb_amount_list),2)
                #京东消费次数
                self.shop_map_ful["jd_shop_cnt"] = sum(jd_cnt_list)
                #京东消费金额
                self.shop_map_ful["jd_expense_amount"] = round(sum(jd_amount_list),2)
                #最大地址改变次数
                self.shop_map_ful["max_change_address_cnt"] = max(max(tb_address_change_list), max(jd_address_change_list))
                #客单价（总金额/总次数
                self.shop_map_ful["amount_per_time"] = round(float(self.shop_map_ful["total_shop_amount"]) / float(self.shop_map_ful["total_shop_cnt"]),2)
                #月均消费频率（总次数/总月份数）
                #self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(max(len(tb_cnt_list),len(jd_cnt_list))),2)
                #淘宝使用年限
                self.shop_map_ful["tb_use_years"] = round(len(tb_month_list) / 12.0,1)
                #京东使用年限
                self.shop_map_ful["jd_use_years"] = round(len(jd_month_list) / 12.0,1)

            elif tb_date:
                #最近月消费次数
                self.shop_map_ful["recently_mon_cnt"] = tb_info[0][3]
                #最近月消费月的金额
                self.shop_map_ful["recently_mon_amount"] = round(tb_info[0][5],2)
                #最大消费月份次数
                self.shop_map_ful["max_mon_cnt"] = max(tb_cnt_list)
                #最小消费月次数
                self.shop_map_ful["min_mon_cnt"] = min(tb_cnt_list)
                #最大消费月份金额
                self.shop_map_ful["max_mon_amount"] = round(max(tb_amount_list),2)
                #最小消费月份金额
                self.shop_map_ful["min_mon_amount"] = round(min(tb_amount_list),2)
                #总消费次数
                self.shop_map_ful["total_shop_cnt"] = sum(tb_cnt_list)
                #总消费金额
                self.shop_map_ful["total_shop_amount"] = round(sum(tb_amount_list),2)
                #淘宝消费次数
                self.shop_map_ful["tb_shop_cnt"] = sum(tb_cnt_list)
                #淘宝消费金额
                self.shop_map_ful["tb_expense_amount"] = round(sum(tb_amount_list),2)
                #最大地址改变次数
                self.shop_map_ful["max_change_address_cnt"] = max(tb_address_change_list)
                #客单价（总金额/总次数）
                self.shop_map_ful["amount_per_time"] = round(float(self.shop_map_ful["total_shop_amount"]) / float(self.shop_map_ful["total_shop_cnt"]),2)
                #self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(len(tb_cnt_list)),2)
                #淘宝使用年限（以消费月为准）
                self.shop_map_ful["tb_use_years"] = round(len(tb_month_list) / 12.0,1)

            elif jd_date:
                #最近月消费月次数
                self.shop_map_ful["recently_mon_cnt"] = jd_info[0][3]
                #最近月消费月的金额
                self.shop_map_ful["recently_mon_amount"] = round(jd_info[0][5],2)
                #最大消费月份次数
                self.shop_map_ful["max_mon_cnt"] = max(jd_cnt_list)
                #最小消费月次数
                self.shop_map_ful["min_mon_cnt"] = min(jd_cnt_list)
                #最大消费月份金额
                self.shop_map_ful["max_mon_amount"] = round(max(jd_amount_list),2)
                #最小消费月份金额
                self.shop_map_ful["min_mon_amount"] = round(min(jd_amount_list),2)
                #总消费次数
                self.shop_map_ful["total_shop_cnt"] = sum(jd_cnt_list)
                #总消费金额
                self.shop_map_ful["total_shop_amount"] = round(sum(jd_amount_list),2)
                #京东消费次数
                self.shop_map_ful["jd_shop_cnt"] = sum(jd_cnt_list)
                #京东消费金额
                self.shop_map_ful["jd_expense_amount"] = round(sum(jd_amount_list),2)
                #最大地址改变次数
                self.shop_map_ful["max_change_address_cnt"] = max(jd_address_change_list)
                #客单价（总金额/总次数）
                self.shop_map_ful["amount_per_time"] = round(float(self.shop_map_ful["total_shop_amount"]) / float(self.shop_map_ful["total_shop_cnt"]),2)
                #self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(len(jd_cnt_list)),2)
                #京东使用年限
                self.shop_map_ful["jd_use_years"] = round(len(jd_month_list) / 12.0,1)
        elif self.shop_map_ful["has_tb_account"] == 1:
            tb_sql = "select create_time from zs_shop_expense where user_id = '%s' " \
                     "and web_site='淘宝' order by id desc limit 1" % user_id
            tb_date = self.db.execute(tb_sql)
            if tb_date:
                date_time = str(tb_date[0][0])
                tb_sql = "select user_id,web_site,`month`,count,change_address_count," \
                         "expense from zs_shop_expense " \
                         "where user_id = '%s' and web_site='淘宝' " \
                         "and create_time='%s' ORDER BY `month` desc " % (user_id, date_time)
                tb_info = self.db.execute(tb_sql)
                if tb_info:
                    self.shop_map_ful["recently_mon_cnt"] = tb_info[0][3]
                    self.shop_map_ful["recently_mon_amount"] = round(tb_info[0][5],2)
                    cnt_list = list()
                    amount_list = list()
                    address_change_list = list()
                    for cell in tb_info:
                        cnt_list.append(cell[3])
                        amount_list.append(cell[5])
                        address_change_list.append(cell[4])
                    #最大消费月份次数
                    self.shop_map_ful["max_mon_cnt"] = max(cnt_list)
                    #最小消费月次数
                    self.shop_map_ful["min_mon_cnt"] = min(cnt_list)
                    #最大消费月金额
                    self.shop_map_ful["max_mon_amount"] = round(max(amount_list),2)
                    #最小消费月金额
                    self.shop_map_ful["min_mon_amount"] = round(min(amount_list),2)
                    #总消费次数
                    self.shop_map_ful["total_shop_cnt"] = sum(cnt_list)
                    #总消费金额
                    self.shop_map_ful["total_shop_amount"] = round(sum(amount_list),2)
                    #淘宝购物次数
                    self.shop_map_ful["tb_shop_cnt"] = sum(cnt_list)
                    #淘宝购物金额
                    self.shop_map_ful["tb_expense_amount"] = round(sum(amount_list),2)
                    #最大地址改变次数
                    self.shop_map_ful["max_change_address_cnt"] = max(address_change_list)
                    #客单价（总金额/总次数）
                    self.shop_map_ful["amount_per_time"] = round(float(self.shop_map_ful["total_shop_amount"]) / float(self.shop_map_ful["total_shop_cnt"]),2)
                    #self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(len(cnt_list)),2)
                    #填报使用年限
                    self.shop_map_ful["tb_use_years"] = round(len(cnt_list) / 12.0,1)
        elif self.shop_map_ful["has_jd_account"] == 1:
            jd_sql = "select create_time from zs_shop_expense where user_id = '%s' " \
                     "and web_site='京东' order by id desc limit 1" % user_id
            jd_date = self.db.execute(jd_sql)
            if jd_date:
                date_time = str(jd_date[0][0])
                jd_sql = "select user_id,web_site,`month`,count,change_address_count," \
                         "expense from zs_shop_expense " \
                         "where user_id = '%s' and web_site='京东' " \
                         "and create_time='%s' ORDER BY `month` desc " % (user_id, date_time)
                jd_info = self.db.execute(jd_sql)
                if jd_info:
                    self.shop_map_ful["recently_mon_cnt"] = jd_info[0][3]
                    self.shop_map_ful["recently_mon_amount"] = round(jd_info[0][5],2)
                    cnt_list = list()
                    amount_list = list()
                    address_change_list = list()
                    for cell in jd_info:
                        cnt_list.append(cell[3])
                        amount_list.append(cell[5])
                        address_change_list.append(cell[4])
                    #最大消费月份次数
                    self.shop_map_ful["max_mon_cnt"] = max(cnt_list)
                    #最小消费月次数
                    self.shop_map_ful["min_mon_cnt"] = min(cnt_list)
                    #最大消费月金额
                    self.shop_map_ful["max_mon_amount"] = round(max(amount_list),2)
                    #最小消费月金额
                    self.shop_map_ful["min_mon_amount"] = round(min(amount_list),2)
                    #总购物次数
                    self.shop_map_ful["total_shop_cnt"] = sum(cnt_list)
                    #总购物金额
                    self.shop_map_ful["total_shop_amount"] = round(sum(amount_list),2)
                    #京东购物次数
                    self.shop_map_ful["jd_shop_cnt"] = sum(cnt_list)
                    #京东购物金额
                    self.shop_map_ful["jd_expense_amount"] = round(sum(amount_list),2)
                    #最大地址改变次数
                    self.shop_map_ful["max_change_address_cnt"] = max(address_change_list)
                    #客单价（总金额/总次数）
                    self.shop_map_ful["amount_per_time"] = round(float(self.shop_map_ful["total_shop_amount"]) / float(self.shop_map_ful["total_shop_cnt"]),2)
                    #self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(len(cnt_list)),2)
                    #京东使用年限
                    self.shop_map_ful["jd_use_years"] = round(len(cnt_list) / 12.0,1)
        if self.shop_map_ful["has_tb_account"] == 1 or self.shop_map_ful["has_jd_account"] == 1:
            # self.set_month_repay_amt(user_id)

            month_sql=" select user_id,`month`,sum(count) as count,sum(expense) as expense " \
                        "from zs_shop_expense where user_id='%s' "\
                        "group by `month` order by `month` desc" % user_id
            month_expense = self.db.execute(month_sql)
            if month_expense:
                month_count_list = list()
                month_expense_list = list()
                for cell in month_expense:
                    month_count_list.append(int(cell[2]))
                    month_expense_list.append(cell[3])
                #最近3月购物金额
                self.shop_map_ful["recently_3mon_amount"] = round(sum(month_expense_list[:3]),2)
                #最近3月购物次数
                self.shop_map_ful["recently_3mon_cnt"] = sum(month_count_list[:3])
                #最近6月购物金额
                self.shop_map_ful["recently_6mon_amount"] = round(sum(month_expense_list[:6]),2)
                #最近6月购物次数
                self.shop_map_ful["recently_6mon_cnt"] = sum(month_count_list[:6])
                #最近一年购物金额
                self.shop_map_ful["recently_year_amount"] = round(sum(month_expense_list[:12]),2)
                #最近一年购物次数
                self.shop_map_ful["recently_year_cnt"] = sum(month_count_list[:12])
                #月均消费频率（总次数/总月份数）
                self.shop_map_ful["times_per_mon"] = round(float(self.shop_map_ful["total_shop_cnt"]) / float(len(month_count_list)),2)
                #异常的月数（超过月还款额的月份）
                #200为虚拟值，需要从数据库读出
                tem_month_repay_amt = self.get_month_repay_amt(user_id) #这个值从生产库拿，每月还款额
                self.shop_map_ful["exception_mons"] = len(filter(lambda x:x>tem_month_repay_amt,month_expense_list))
                #异常的月数占总消费月份的比例
                self.shop_map_ful["exception_mons_rate"] = round(float(self.shop_map_ful["exception_mons"]) / float(len(month_count_list)),2)

    def check_receiver_info_ful(self,user_id):
        #查询真实姓名和电话
        mobile_sql = " select user_id,`name`,mobile from zs_shop_base where user_id = '%s'" % user_id
        mobile_info = self.db.execute(mobile_sql)
        if mobile_info:
            name_set = set()
            mobile_set = set()
            for cell in mobile_info:
                if cell[1]:
                    name_set.add(str(cell[1].encode('utf-8')))
                if cell[2]:
                    mobile_set.add(str(cell[2]))
                    # 加入有星号电话
                    mobile_set.add(cell[2][:3]+'****'+cell[2][-4:])

            receiver_sql = "select user_id,`name`,phone,count,amount "\
                        "from zs_shop_address_receiver where user_id = '%s'" % user_id
            receiver_info = self.db.execute(receiver_sql)
            if receiver_info:
                virtual_pro_count = list()
                virtual_pro_amount = list()
                receiver_notself_count = list()
                receiver_notself_amount = list()
                receiver_nickname_count = list()
                virtualreceiver_set = set(('不需收货人','不需要收货人'))
                for cell in receiver_info:
                    if cell[1] and (cell[1].encode('utf-8') in virtualreceiver_set):
                        virtual_pro_count.append(cell[3])
                        virtual_pro_amount.append(cell[4])
                    if cell[1] and cell[2] and (cell[1].encode('utf-8') not in virtualreceiver_set) and (str(cell[2].encode('utf-8')) not in mobile_set):
                        receiver_notself_count.append(cell[3])
                        receiver_notself_amount.append(cell[4])

                    if cell[2] and cell[1] and (str(cell[2].encode('utf-8')) in mobile_set) and (str(cell[1].encode('utf-8')) not in name_set):
                        receiver_nickname_count.append(cell[3])
                #虚拟产品消费的次数
                self.shop_map_ful['virtual_shop_cnt'] = sum(virtual_pro_count)
                #虚拟产品消费的金额
                self.shop_map_ful['virtual_shop_amount'] = round(sum(virtual_pro_amount),2)
                #虚拟产品消费次数占总消费次数的比例
                self.shop_map_ful['virtual_shop_rate'] = round(float(self.shop_map_ful['virtual_shop_cnt']) / self.shop_map_ful['total_shop_cnt'],2)
                #非虚拟产品消费的次数
                self.shop_map_ful['non_virtual_shop_cnt'] = self.shop_map_ful['total_shop_cnt'] - self.shop_map_ful['virtual_shop_cnt']
                #非虚拟产品消费的金额
                self.shop_map_ful['non_virtual_shop_amount'] = self.shop_map_ful['total_shop_amount'] - self.shop_map_ful['virtual_shop_amount']
                #收货人是否有非本人的情况
                self.shop_map_ful['is_receiver_not_self'] = 1 if len(receiver_notself_count) > 0 else 0
                #收货人是否使用昵称（化名）
                self.shop_map_ful['is_receiver_nickname'] = 1 if len(receiver_nickname_count) > 0 else 0
                #收货人非本人的次数
                self.shop_map_ful['receiver_notself_cnt'] = sum(receiver_notself_count)
                #收货人非本人的金额
                self.shop_map_ful['receiver_notself_amount'] = round(sum(receiver_notself_amount),2)

    def _save_data_ful(self, user_id):
        self.it_db.insert('zs_shop_etl_copy',{'user_id':user_id,
                                      'is_use_blanknote':str(self.shop_map_ful["is_use_blanknote"]),
                                      'use_blanknote_rate':str(self.shop_map_ful["use_blanknote_rate"]),
                                      'use_blanknote_amount':str(self.shop_map_ful["use_blanknote_amount"]),
                                      'blank_note':str(self.shop_map_ful["blank_note"]),
                                      'blank_note_balance':str(self.shop_map_ful["blank_note_balance"]),
                                      'recently_mon_cnt':str(self.shop_map_ful["recently_mon_cnt"]),
                                      'recently_mon_amount':str(self.shop_map_ful["recently_mon_amount"]),
                                      'recently_3mon_amount':str(self.shop_map_ful["recently_3mon_amount"]),
                                      'recently_3mon_cnt':str(self.shop_map_ful["recently_3mon_cnt"]),
                                      'recently_6mon_amount':str(self.shop_map_ful["recently_6mon_amount"]),
                                      'recently_6mon_cnt':str(self.shop_map_ful["recently_6mon_cnt"]),
                                      'recently_year_amount':str(self.shop_map_ful["recently_year_amount"]),
                                      'recently_year_cnt':str(self.shop_map_ful["recently_year_cnt"]),
                                      'recently_shop_days':str(self.shop_map_ful["recently_shop_days"]),
                                      'max_mon_cnt':str(self.shop_map_ful["max_mon_cnt"]),
                                      'max_mon_amount':str(self.shop_map_ful["max_mon_amount"]),
                                      'min_mon_cnt':str(self.shop_map_ful["min_mon_cnt"]),
                                      'min_mon_amount':str(self.shop_map_ful["min_mon_amount"]),
                                      'exception_mons':str(self.shop_map_ful["exception_mons"]),
                                      'exception_mons_rate':str(self.shop_map_ful["exception_mons_rate"]),
                                      'amount_per_time':str(self.shop_map_ful["amount_per_time"]),
                                      'times_per_mon':str(self.shop_map_ful["times_per_mon"]),
                                      'total_shop_cnt':str(self.shop_map_ful["total_shop_cnt"]),
                                      'total_shop_amount':str(self.shop_map_ful["total_shop_amount"]),
                                      'sum_addresses':str(self.shop_map_ful["sum_addresses"]),
                                      'max_address_cnt':str(self.shop_map_ful["max_address_cnt"]),
                                      'max_address_amount':str(self.shop_map_ful["max_address_amount"]),
                                      'min_address_cnt':str(self.shop_map_ful["min_address_cnt"]),
                                      'min_address_amount':str(self.shop_map_ful["min_address_amount"]),
                                      'total_address_cnt':str(self.shop_map_ful["total_address_cnt"]),
                                      'shop_one_address_cnt':str(self.shop_map_ful["shop_one_address_cnt"]),
                                      'max_address_between_days':str(self.shop_map_ful["max_address_between_days"]),
                                      'min_address_between_days':str(self.shop_map_ful["min_address_between_days"]),
                                      'max_change_address_cnt':str(self.shop_map_ful["max_change_address_cnt"]),
                                      'virtual_shop_cnt':str(self.shop_map_ful["virtual_shop_cnt"]),
                                      'virtual_shop_amount':str(self.shop_map_ful["virtual_shop_amount"]),
                                      'virtual_shop_rate':str(self.shop_map_ful["virtual_shop_rate"],),
                                      'non_virtual_shop_cnt':str(self.shop_map_ful["non_virtual_shop_cnt"]),
                                      'non_virtual_shop_amount':str(self.shop_map_ful["non_virtual_shop_amount"]),
                                      'is_receiver_not_self':str(self.shop_map_ful["is_receiver_not_self"]),
                                      'is_receiver_nickname':str(self.shop_map_ful["is_receiver_nickname"]),
                                      'receiver_notself_cnt':str(self.shop_map_ful["receiver_notself_cnt"]),
                                      'receiver_notself_amount':str(self.shop_map_ful["receiver_notself_amount"]),
                                      'is_use_qqmail':str(self.shop_map_ful["is_use_qqmail"]),
                                      'is_use_vip_qqmail':str(self.shop_map_ful["is_use_vip_qqmail"]),
                                      'is_use_nickname_qqmail':str(self.shop_map_ful["is_use_nickname_qqmail"]),
                                      'length_qq':str(self.shop_map_ful["length_qq"]),
                                      'tb_use_years':str(self.shop_map_ful["tb_use_years"]),
                                      'jd_use_years':str(self.shop_map_ful["jd_use_years"]),
                                      'has_jd_account':str(self.shop_map_ful["has_jd_account"]),
                                      'has_tb_account':str(self.shop_map_ful["has_tb_account"]),
                                      'tb_is_identity':str(self.shop_map_ful["tb_is_identity"]),
                                      'jd_is_identity':str(self.shop_map_ful["jd_is_identity"]),
                                      'tb_shop_cnt':str(self.shop_map_ful["tb_shop_cnt"]),
                                      'jd_shop_cnt':str(self.shop_map_ful["jd_shop_cnt"]),
                                      'jd_expense_amount':str(self.shop_map_ful["jd_expense_amount"]),
                                      'tb_expense_amount':str(self.shop_map_ful["tb_expense_amount"]),
                                      'create_time':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                       )

    def request_proc(self, user_id):
        self.check_shop_account_ful(user_id)
        self.set_blank_note_ful(user_id)
        self.check_address_info_ful(user_id)
        self.check_mon_info_ful(user_id)
        self.check_receiver_info_ful(user_id)
        self._save_data_ful(user_id)
        return self.shop_map_ful

def save_by_chunk(chunksize=1000):
    test_file = pd.read_table(r'data_zuixin.txt',chunksize=chunksize)
    outer_=0
    current_postion=0
    for chunk in test_file:
        print 'chunk position: %d' % outer_
        for i in range(len(chunk)):
            current_postion = outer_*chunksize+i+1
            # if current_postion < 40967:
            #     continue
            print 'chunk position: %d' % outer_
            print 'dataframe index %d' % i
            print 'cust_no %s' % 'szbyjr_'+chunk.iloc[i,0].split(',')[0]
            ShopHandler().request_proc('szbyjr_'+chunk.iloc[i,0].split(',')[0])
        outer_+=1

if __name__ == "__main__":
    # db_client = configs.config.mysql_edw
    # db_host = db_client["host"]
    # db_user = db_client["user"]
    # db_password = db_client["passwd"]
    # db_name = db_client["db"]
    # db.bind("mysql", host=db_host, user=db_user, passwd=db_password, db=db_name)
    # db.generate_mapping(create_tables=True)
    # """
    # user_id = {"user_id":"szbyjr_596549"}
    # start_time = time.time()
    # res_info = ShopHandler().request_proc(user_id)
    # end_time = time.time()
    # time_period = end_time-start_time
    # print time_period
    # """
    # line_list = list()
    # f = open("user_id_170519.txt","r")             # 返回一个文件对象
    # line = f.readline()             # 调用文件的 readline()方法
    # while line:
    #     line = f.readline().strip("\r\n")
    #     if line:
    #         line_list.append("szbyjr_"+line)
    # line_list= list(set(line_list))
    # f.close()
    # for user in line_list:
    #     user_id = {"user_id":user}
    #     print user_id
    #     res_info = ShopHandler().request_proc(user_id)
    #     print res_info
    #user_id = {"user_id":"szbyjr_596549"}
    # start_time = time.time()
    # res_info = ShopHandler().request_proc('szbyjr_784019')
    # end_time = time.time()
    # time_period = end_time-start_time
    # print time_period
    # print res_info
    # for key,value in res_info.iteritems():
    #    print key+" : "+str(value)
    # import random

    # test_file = open(r'test_data_userid_all.txt')
    # userid_list = test_file.readlines()
    # random.shuffle(userid_list)
    # #userid_test = random.sample(userid_list,50)
    # for i in range(len(userid_list)):
    #     print i
    #     print userid_list[i]
    #     feature_info = ShopHandler().request_proc(userid_list[i].replace('"','').strip())
    #     for key,value in feature_info.iteritems():
    #         print key+" : "+str(value)
    for id in ('szbyjr_1737872'):
        ShopHandler().request_proc(id)