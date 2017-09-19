# -*- coding: utf-8 -*-

import pymysql
#constant varanbles
DEFAUL_VALE=-999

#月还款额，需要从数据库读出
MONTH_REPAY_AMOUNT=200

config={
	'zs_shop_map' : {
    "has_jd_account": -999,  # 是否有京东账号
    "has_tb_account": -999,  # 是否有淘宝账号
    "tb_is_identity": -999,  # 淘宝是否实名认证
    "jd_is_identity": -999,  # 京东是否实名认证
    "is_use_qqmail": -999, # 是否使用QQ邮箱
    "is_use_vip_qqmail": -999, # 是否使用QQ vip邮箱
    "is_use_nickname_qqmail": -999, # QQ邮箱是否使用昵称
    "length_qq": -999, # QQ号的长度
    "tb_use_years": -999, # 淘宝使用年限
    "jd_use_years": -999, # 京东使用年限

    "total_shop_cnt": -999,  # 总消费次数
    "total_shop_amount": -999,  # 总消费金额
    "tb_shop_cnt": -999,  # 淘宝消费次数
    "jd_shop_cnt": -999,  # 京东消费次数
    "jd_expense_amount": -999,  # 京东消费金额
    "tb_expense_amount": -999,  # 淘宝消费金额
    "max_address_cnt": -999,  # 地址对应最大消费次
    "max_address_amount": -999,  # 地址对应最大消费金额
    "min_address_cnt": -999,  # 地址对应最小消费次数
    "min_address_amount": -999,  # 地址对应最小消费金额
    "total_address_cnt": -999,  # 地址对应消费次数总和
    "shop_one_address_cnt": -999,  # 只消费过一次的地址个数
    "max_address_between_days": -999,  # 地址消费最大间隔时间
    "min_address_between_days": -999,  # 地址消费最小间隔时间
    "sum_addresses": -999, # 地址总数

    "blank_note": -999,  # 白条授信额度
    "blank_note_balance": -999,  # 白条可用额度
    "is_use_blanknote": -999, # 是否使用过白条
    "use_blanknote_rate": -999, # 使用比例
    "use_blanknote_amount": -999, # 已使用额度

    "max_mon_cnt": -999,  # 最大消费月份次数
    "max_mon_amount": -999,  # 最大消费月份金额
    "min_mon_cnt": -999,  # 最小消费月次数
    "min_mon_amount": -999,  # 最小消费月份金额
    "recently_mon_from_now": -999,  # 无用
    "recently_mon_cnt": -999,  # 最近消费月次数
    "recently_mon_amount": -999,  # 最近消费月的金额   
    "max_change_address_cnt": -999,  # 最大地址改变次数
    "recently_3mon_amount": -999, # 最近3个月的消费金额
    "recently_3mon_cnt": -999, # 最近3个月的消费次数
    "recently_6mon_amount": -999, # 最近6个月的消费金额
    "recently_6mon_cnt": -999, # 最近6个月的消费次数
    "recently_year_amount": -999, # 最近一年的消费金额
    "recently_year_cnt": -999, # 最近一年的消费次数
    "recently_shop_days": -999, # 最近一次购物距离现在的天数
    "exception_mons": -999, # 异常的月数（超过月还款额的月份）
    "exception_mons_rate": -999, # 异常的月数占总消费月份的比例
    "amount_per_time": -999, # 客单价（总金额/总次数）
    "times_per_mon": -999, # 月均消费频率（总次数/总月份数）
    
    "virtual_shop_cnt": -999, # 虚拟产品消费的次数
    "virtual_shop_amount": -999, # 虚拟产品消费的金额
    "virtual_shop_rate": -999, # 虚拟产品消费次数占总消费次数的比例
    "non_virtual_shop_cnt": -999,# 非虚拟产品消费的次数
    "non_virtual_shop_amount": -999, # 非虚拟产品消费的金额
    "is_receiver_not_self": -999, # 收货人是否有非本人的情况
    "is_receiver_nickname": -999, # 收货人是否使用昵称（化名）
    "receiver_notself_cnt": -999, #  收货人非本人的次数
    "receiver_notself_amount": -999, # 收货人非本人的金额


    },



    # 生产库权限
    'pro_db':{
    'host':'120.27.204.100',
    'port':3306,
    'user':'Developer',
    'password':'027675b0-6c2f-11e7-8ea9-185e0f52d4e6',
    'database':'edw',
    'charset':'utf8'
    },

    'db':{
    'host':'120.27.204.100',
    'port':3306,
    'user':'Developer',
    'password':'027675b0-6c2f-11e7-8ea9-185e0f52d4e6',
    'database':'edw',
    'charset':'utf8'
   # 'cursorclass':pymysql.cursors.DictCursor

    },
    #数据挖掘库
    'data_save_db':{
    'host':'120.27.204.100',
    'port':3306,
    'user':'Developer',
    'password':'027675b0-6c2f-11e7-8ea9-185e0f52d4e6',
    'database':'DataMining',
    'charset':'utf8'
    },

    'month_repay_amt':200

}
