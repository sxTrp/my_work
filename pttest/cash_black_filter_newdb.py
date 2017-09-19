# -*- coding: utf-8 -*-

"""
modules: White_Rule_Credit
Date:    2016/11/16
"""

import sys
import os
import cx_Oracle
import time
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("/home/ash/app/batch_model/cash_white_rules_v1/")
sys.path.append("/home/ash/app/batch_model/cash_white_rules_v1/jf_rules/")
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import urllib2
import json
from commons.common import JvmManager
from conf import settings
from helper import JFBlackQueryAPI
import MySQLdb
from datetime import datetime

class WhiteRuleCredit(object):

    @classmethod
    def make_data_sql(self, id_cards, phonelist):
        try:
            info_sql = """
select ttt.id,ttt.cust_name,ttt.cert_no,ttt.PHONE_NO,ttt.cust_sex,
ttt.address,'交叉现金贷（特殊）' tel_prod,'50215' prod_code,ttt.credit_line,now() operate_date,
'01060005' operater,'博雅名单' data_source
from(
select UUID() id,aa.cert_no,bb.credit_amt credit_line,bb.address,bb.cust_sex,bb.cust_age,bb.cust_income,bb.phone_no,bb.cust_name from (
select cert_no,rule from(
select tt2.cert_no,(case when tt4.prod_no in ('20015','20017','50014','50015','50016','50017','50018','50022','50023','50214',
'50215','50216','50217','50223','60001','60002','60201','60202') then '现金贷' else '消费贷' end) prod_name,case when tt3.normal_rule in (1,2) or tt3.tq_rule in (1,2,3,4) then 0 else 1 end rule from b_lo_loan_info tt1
					LEFT JOIN b_lo_cust_info tt2 on tt1.cust_no=tt2.cust_no
					LEFT JOIN(
					select loan_no,case when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq<=7 then 1
											when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq>=8 and max_yq<=15 then 2 else 0 end normal_rule,
											case when jq_rule =1 and tq_repay_num<=3 and yq_cnt=0 then 1
													 when jq_rule =1 and tq_repay_num>3 and tq_repay_num<=6 and yq_cnt<=2 then 2
													 when jq_rule =1 and tq_repay_num>6 and tq_repay_num<=12 and max_yq<=5 and total_yq<=20 then 3
													 when jq_rule =1 and tq_repay_num>12 and tq_repay_num<=12 and max_yq<=10 and total_yq<=30 then 4 else 0 end tq_rule
						from(
						select loan_no,case when repay_num<install_num then  0  when repay_num=install_num and tq_num=0 then 0
										when repay_num=install_num and tq_num!=0 then 1 end jq_rule,install_num,repay_num,max_yq,total_yq,install_num-tq_num tq_repay_num,yq_cnt
						from (
						select loan_no,max(aaa.repay_num) install_num,sum(aaa.is_repay) repay_num,sum(aaa.tq_num) tq_num,
							max(yq_num) max_yq,sum(case when yq_num<=0 then 0 else yq_num end) total_yq,
							sum(case when yq_num<=0 then 0 else 1 end) yq_cnt
							from(
							select aa.*,case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then DATEDIFF(aa.TRANS_DATE,aa.REPAY_DATE)
							else DATEDIFF(DATE_FORMAT(now(),'%Y%m%d'),aa.REPAY_DATE) end yq_num,
							case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then 1 else 0 end is_repay,
							case when DATE_FORMAT(aa.TRANS_DATE,'%Y%m%d')<aa.REPAY_DATE then 1 else 0 end tq_num
							from c_acc_loan_acct_stat aa
							) aaa GROUP BY loan_no ) aa1
					) t1 )tt3 on tt1.loan_no=tt3.loan_no
					left join b_lo_loan_prod tt4 on tt1.loan_no=tt4.loan_no
					) tt where rule=0 and prod_name='消费贷' limit 6000
) aa
LEFT JOIN (
	select cert_no,case when  score>='650' then '30000' when score>='550' and score<'650' then '25000'
            when score>='530' and score<'550' then '21000' when score>='510' and score<'530' then '18000'
            when score>='470' and score<'510' then '17000' else '15000' end credit_amt,address,cust_sex,cust_age,cust_income,phone_no,cust_name from (
	select cert_no,max(LOAN_SCORE) score,max(address) address,max(cust_sex) cust_sex,max(cust_age) cust_age,max(cust_income) cust_income,max(phone_no) phone_no,max(cust_name) cust_name from (
	select t3.CERT_NO,t1.LOAN_SCORE,concat(t5.PROV_NAME,t5.CITY_NAME,t5.AREA_NAME,t4.LIVE_ADDR) address,t3.SEX cust_sex,
	ROUND(DATEDIFF(now(),DATE_FORMAT(SUBSTR(t3.CERT_NO,7,8),'%Y-%m-%d'))/365) as cust_age,t3.cust_name,t6.INCOME cust_income,t7.phone_no from b_9f_loan_order_info t1
	LEFT JOIN b_lo_loan_info t2 on t1.loan_no=t2.loan_no
	LEFT JOIN b_lo_cust_info t3 on t2.cust_no=t3.cust_no
	LEFT JOIN b_lo_cust_live_info t4 on t2.cust_no=t4.cust_no
	LEFT JOIN a_sys_regional_belong t5 on t4.LIVE_PROV=t5.PROV_NO and t4.LIVE_CITY=t5.CITY_NO and t4.LIVE_AREA=t5.AREA_NO
	LEFT JOIN b_lo_cust_other_info t6 on t2.cust_no=t6.cust_no
	LEFT JOIN b_lo_cust_contct_info t7 on t2.cust_no=t7.cust_no
	) t1 group by cert_no ) t2
) bb on aa.cert_no=bb.cert_no
LEFT JOIN ash_out_cust_source cc on aa.cert_no=cc.cert_no
where cc.CERT_NO is null
) ttt
"""
            info_sql1 = """
insert into ash_out_cust_source(id,name,cert_no,phone_no)
select ttt.id,ttt.cust_name,ttt.cert_no,ttt.PHONE_NO
from(
select UUID() id,aa.cert_no,bb.credit_amt credit_line,bb.address,bb.cust_sex,bb.cust_age,bb.cust_income,bb.phone_no,bb.cust_name from (
select cert_no,rule from(
select tt2.cert_no,(case when tt4.prod_no in ('20015','20017','50014','50015','50016','50017','50018','50022','50023','50214',
'50215','50216','50217','50223','60001','60002','60201','60202') then '现金贷' else '消费贷' end) prod_name,case when tt3.normal_rule in (1,2) or tt3.tq_rule in (1,2,3,4) then 0 else 1 end rule from b_lo_loan_info tt1
					LEFT JOIN b_lo_cust_info tt2 on tt1.cust_no=tt2.cust_no
					LEFT JOIN(
					select loan_no,case when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq<=7 then 1
											when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq>=8 and max_yq<=15 then 2 else 0 end normal_rule,
											case when jq_rule =1 and tq_repay_num<=3 and yq_cnt=0 then 1
													 when jq_rule =1 and tq_repay_num>3 and tq_repay_num<=6 and yq_cnt<=2 then 2
													 when jq_rule =1 and tq_repay_num>6 and tq_repay_num<=12 and max_yq<=5 and total_yq<=20 then 3
													 when jq_rule =1 and tq_repay_num>12 and tq_repay_num<=12 and max_yq<=10 and total_yq<=30 then 4 else 0 end tq_rule
						from(
						select loan_no,case when repay_num<install_num then  0  when repay_num=install_num and tq_num=0 then 0
										when repay_num=install_num and tq_num!=0 then 1 end jq_rule,install_num,repay_num,max_yq,total_yq,install_num-tq_num tq_repay_num,yq_cnt
						from (
						select loan_no,max(aaa.repay_num) install_num,sum(aaa.is_repay) repay_num,sum(aaa.tq_num) tq_num,
							max(yq_num) max_yq,sum(case when yq_num<=0 then 0 else yq_num end) total_yq,
							sum(case when yq_num<=0 then 0 else 1 end) yq_cnt
							from(
							select aa.*,case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then DATEDIFF(aa.TRANS_DATE,aa.REPAY_DATE)
							else DATEDIFF(DATE_FORMAT(now(),'%Y%m%d'),aa.REPAY_DATE) end yq_num,
							case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then 1 else 0 end is_repay,
							case when DATE_FORMAT(aa.TRANS_DATE,'%Y%m%d')<aa.REPAY_DATE then 1 else 0 end tq_num
							from c_acc_loan_acct_stat aa
							) aaa GROUP BY loan_no ) aa1
					) t1 )tt3 on tt1.loan_no=tt3.loan_no
					left join b_lo_loan_prod tt4 on tt1.loan_no=tt4.loan_no
					) tt where rule=0 and prod_name='消费贷' limit 6000
) aa
LEFT JOIN (
	select cert_no,case when  score>='650' then '30000' when score>='550' and score<'650' then '25000'
            when score>='530' and score<'550' then '21000' when score>='510' and score<'530' then '18000'
            when score>='470' and score<'510' then '17000' else '15000' end credit_amt,address,cust_sex,cust_age,cust_income,phone_no,cust_name from (
	select cert_no,max(LOAN_SCORE) score,max(address) address,max(cust_sex) cust_sex,max(cust_age) cust_age,max(cust_income) cust_income,max(phone_no) phone_no,max(cust_name) cust_name from (
	select t3.CERT_NO,t1.LOAN_SCORE,concat(t5.PROV_NAME,t5.CITY_NAME,t5.AREA_NAME,t4.LIVE_ADDR) address,t3.SEX cust_sex,
	ROUND(DATEDIFF(now(),DATE_FORMAT(SUBSTR(t3.CERT_NO,7,8),'%Y-%m-%d'))/365) as cust_age,t3.cust_name,t6.INCOME cust_income,t7.phone_no from b_9f_loan_order_info t1
	LEFT JOIN b_lo_loan_info t2 on t1.loan_no=t2.loan_no
	LEFT JOIN b_lo_cust_info t3 on t2.cust_no=t3.cust_no
	LEFT JOIN b_lo_cust_live_info t4 on t2.cust_no=t4.cust_no
	LEFT JOIN a_sys_regional_belong t5 on t4.LIVE_PROV=t5.PROV_NO and t4.LIVE_CITY=t5.CITY_NO and t4.LIVE_AREA=t5.AREA_NO
	LEFT JOIN b_lo_cust_other_info t6 on t2.cust_no=t6.cust_no
	LEFT JOIN b_lo_cust_contct_info t7 on t2.cust_no=t7.cust_no
	) t1 group by cert_no ) t2
) bb on aa.cert_no=bb.cert_no
LEFT JOIN ash_out_cust_source cc on aa.cert_no=cc.cert_no
where cc.CERT_NO is null
) ttt
"""
            return info_sql
        except Exception, e:
            raise e

    @classmethod
    def check_sql(self):
        try:
            check_sql = """
select ttt.cust_name,ttt.cert_no,ttt.PHONE_NO,ttt.cust_sex,
ttt.address,'交叉现金贷（特殊）' tel_prod,'50215' prod_code,ttt.credit_line,now() operate_date,
'01060005' operater,'博雅名单' data_source
from(
select UUID() id,aa.cert_no,bb.credit_amt credit_line,bb.address,bb.cust_sex,bb.cust_age,bb.cust_income,bb.phone_no,bb.cust_name from (
select cert_no,rule from(
select tt2.cert_no,(case when tt4.prod_no in ('20015','20017','50014','50015','50016','50017','50018','50022','50023','50214',
'50215','50216','50217','50223','60001','60002','60201','60202') then '现金贷' else '消费贷' end) prod_name,case when tt3.normal_rule in (1,2) or tt3.tq_rule in (1,2,3,4) then 0 else 1 end rule from b_lo_loan_info tt1
					LEFT JOIN b_lo_cust_info tt2 on tt1.cust_no=tt2.cust_no
					LEFT JOIN(
					select loan_no,case when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq<=7 then 1
											when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq>=8 and max_yq<=15 then 2 else 0 end normal_rule,
											case when jq_rule =1 and tq_repay_num<=3 and yq_cnt=0 then 1
													 when jq_rule =1 and tq_repay_num>3 and tq_repay_num<=6 and yq_cnt<=2 then 2
													 when jq_rule =1 and tq_repay_num>6 and tq_repay_num<=12 and max_yq<=5 and total_yq<=20 then 3
													 when jq_rule =1 and tq_repay_num>12 and tq_repay_num<=12 and max_yq<=10 and total_yq<=30 then 4 else 0 end tq_rule
						from(
						select loan_no,case when repay_num<install_num then  0  when repay_num=install_num and tq_num=0 then 0
										when repay_num=install_num and tq_num!=0 then 1 end jq_rule,install_num,repay_num,max_yq,total_yq,install_num-tq_num tq_repay_num,yq_cnt
						from (
						select loan_no,max(aaa.repay_num) install_num,sum(aaa.is_repay) repay_num,sum(aaa.tq_num) tq_num,
							max(yq_num) max_yq,sum(case when yq_num<=0 then 0 else yq_num end) total_yq,
							sum(case when yq_num<=0 then 0 else 1 end) yq_cnt
							from(
							select aa.*,case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then DATEDIFF(aa.TRANS_DATE,aa.REPAY_DATE)
							else DATEDIFF(DATE_FORMAT(now(),'%Y%m%d'),aa.REPAY_DATE) end yq_num,
							case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then 1 else 0 end is_repay,
							case when DATE_FORMAT(aa.TRANS_DATE,'%Y%m%d')<aa.REPAY_DATE then 1 else 0 end tq_num
							from c_acc_loan_acct_stat aa
							) aaa GROUP BY loan_no ) aa1
					) t1 )tt3 on tt1.loan_no=tt3.loan_no
					left join b_lo_loan_prod tt4 on tt1.loan_no=tt4.loan_no
					) tt where rule=0 and prod_name='消费贷' limit 6000
) aa
LEFT JOIN (
	select cert_no,case when  score>='650' then '30000' when score>='550' and score<'650' then '25000'
            when score>='530' and score<'550' then '21000' when score>='510' and score<'530' then '18000'
            when score>='470' and score<'510' then '17000' else '15000' end credit_amt,address,cust_sex,cust_age,cust_income,phone_no,cust_name from (
	select cert_no,max(LOAN_SCORE) score,max(address) address,max(cust_sex) cust_sex,max(cust_age) cust_age,max(cust_income) cust_income,max(phone_no) phone_no,max(cust_name) cust_name from (
	select t3.CERT_NO,t1.LOAN_SCORE,concat(t5.PROV_NAME,t5.CITY_NAME,t5.AREA_NAME,t4.LIVE_ADDR) address,t3.SEX cust_sex,
	ROUND(DATEDIFF(now(),DATE_FORMAT(SUBSTR(t3.CERT_NO,7,8),'%Y-%m-%d'))/365) as cust_age,t3.cust_name,t6.INCOME cust_income,t7.phone_no from b_9f_loan_order_info t1
	LEFT JOIN b_lo_loan_info t2 on t1.loan_no=t2.loan_no
	LEFT JOIN b_lo_cust_info t3 on t2.cust_no=t3.cust_no
	LEFT JOIN b_lo_cust_live_info t4 on t2.cust_no=t4.cust_no
	LEFT JOIN a_sys_regional_belong t5 on t4.LIVE_PROV=t5.PROV_NO and t4.LIVE_CITY=t5.CITY_NO and t4.LIVE_AREA=t5.AREA_NO
	LEFT JOIN b_lo_cust_other_info t6 on t2.cust_no=t6.cust_no
	LEFT JOIN b_lo_cust_contct_info t7 on t2.cust_no=t7.cust_no
	) t1 group by cert_no ) t2
) bb on aa.cert_no=bb.cert_no
LEFT JOIN ash_out_cust_source cc on aa.cert_no=cc.cert_no
where cc.CERT_NO is null
) ttt """
            return check_sql
        except Exception, e:
            raise e

    def check_db_sql(self, cert_no, phone):
        check_cert_no = """select cert_no from bycx.T_RECEIVE_LOAN_CONDITION@bycx  where cert_no='%s' """ %cert_no
        check_phone = """select phone_no from bycx.T_RECEIVE_LOAN_CONDITION@bycx  where phone_no='%s' """ %phone
        con = cx_Oracle.connect('edw', '123com', '10.45.22.96:1521/ORCL')
        db = con.cursor()
        db.execute(check_cert_no)
        cert_no = db.fetchall()
        db.execute(check_phone)
        phone_no = db.fetchall()
        db.close()
        con.close()
        if cert_no:
            cert_no = cert_no[0][0]
        else:
            cert_no = ""
        if phone_no:
            phone_no = phone_no[0][0]
        else:
            phone_no = ""
        return cert_no, phone_no


    def get_jf_black(self, rows):
        id_cards = ""
        phonelist = ""
        if rows:
            for row in rows:
                res = JFBlackQueryAPI.query_jfblack_api(row[1], row[0])
                if res["value"] == '1':
                    s = "'"+res["cert_no"]+"',"
                    id_cards += s
                self.save_black_data(row,res["value"])
                cert_no, phone_no = WhiteRuleCredit().check_db_sql(row[1], row[5])
                if cert_no:
                    s = "'"+cert_no+"',"
                    id_cards += s
                if phone_no:
                    s = "'" + phone_no + "',"
                    phonelist += s
        if id_cards:
            id_cards = id_cards[0:len(id_cards)-1]
        if phonelist:
            phonelist = phonelist[0:len(phonelist)-1]
        return id_cards, phonelist

    @classmethod
    def get_rule_data(self):
        
        check_sql = WhiteRuleCredit().check_sql()
        con = MySQLdb.connect(host="10.27.113.75", user="bycx_bi", passwd="bycx_bi", db="bycx_bi")
        db = con.cursor()
        db.execute(check_sql)
        rows = db.fetchall()
        print len(rows)

        id_cards, phonelist = WhiteRuleCredit().get_jf_black(rows)
        db.close()
        con.close()
        WhiteRuleCredit().excute(id_cards, phonelist)

    def check_import_rule(self):
    	pass

    def check_newdatabase_rules(self,cert_no):
    	sql = """select tt2.cert_no,case when tt3.normal_rule in (1,2) or tt3.tq_rule in (1,2,3,4) then 0 else 1 end rule from b_lo_loan_info tt1
					LEFT JOIN b_lo_cust_info tt2 on tt1.cust_no=tt2.cust_no
					LEFT JOIN(
					select loan_no,case when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq<=7 then 1
											when jq_rule =0 and repay_num>=5 and (repay_num/install_num)>=0.33 and max_yq>=8 and max_yq<=15 then 2 else 0 end normal_rule,
											case when jq_rule =1 and tq_repay_num<=3 and yq_cnt=0 then 1
													 when jq_rule =1 and tq_repay_num>3 and tq_repay_num<=6 and yq_cnt<=2 then 2
													 when jq_rule =1 and tq_repay_num>6 and tq_repay_num<=12 and max_yq<=5 and total_yq<=20 then 3
													 when jq_rule =1 and tq_repay_num>12 and tq_repay_num<=12 and max_yq<=10 and total_yq<=30 then 4 else 0 end tq_rule
						from(
						select loan_no,case when repay_num<install_num then  0  when repay_num=install_num and tq_num=0 then 0
										when repay_num=install_num and tq_num!=0 then 1 end jq_rule,install_num,repay_num,max_yq,total_yq,install_num-tq_num tq_repay_num,yq_cnt
						from (
						select loan_no,max(aaa.repay_num) install_num,sum(aaa.is_repay) repay_num,sum(aaa.tq_num) tq_num,
							max(yq_num) max_yq,sum(case when yq_num<=0 then 0 else yq_num end) total_yq,
                            sum(case when yq_num<=0 then 0 else 1 end) yq_cnt
							from(
							select aa.*,case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then DATEDIFF(aa.TRANS_DATE,aa.REPAY_DATE)
							else DATEDIFF(DATE_FORMAT(now(),'%Y%m%d'),aa.REPAY_DATE) end yq_num,
							case when aa.RCV_TOTAL_AMT=aa.ACT_TOTAL_AMT then 1 else 0 end is_repay,
							case when DATE_FORMAT(aa.TRANS_DATE,'%Y%m%d')<aa.REPAY_DATE then 1 else 0 end tq_num
							from c_acc_loan_acct_stat aa
							) aaa GROUP BY loan_no ) aa1
					) t1 )tt3 on tt1.loan_no=tt3.loan_no"""+ """ where tt2.cert_no='%s' """%cert_no
        #print sql
        con = MySQLdb.connect(host="10.27.113.75", user="bycx_bi", passwd="bycx_bi", db="bycx_bi")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        con.close()
        if rows:
            res = list(rows[0])
        else:
            res = []
        return res

    def excute(self,id_cards, phonelist):
        try:
            con = MySQLdb.connect(host='10.27.113.75', user='bycx_bi', passwd='bycx_bi', db='bycx_bi', charset='utf8')
            cursor = con.cursor()
            info_sql = WhiteRuleCredit.make_data_sql(id_cards, phonelist)
            if id_cards != "" and phonelist != "":
                info_sql = info_sql + """ where ttt.cert_no not in ("""+id_cards+""") """
                #info_sql1 = info_sql1 + """ where ttt.cert_no not in ("""+id_cards+""") """
                info_sql = info_sql + """ and ttt.phone_no not in (""" + phonelist +""")"""
                #info_sql1 = info_sql1 + """ and ttt.phone_no not in ("""+phonelist+""") """
            elif id_cards != "":
                info_sql = info_sql + """ where ttt.cert_no not in ("""+id_cards+""") """
                #info_sql1 = info_sql1 + """ where ttt.cert_no not in ("""+id_cards+""") """
            elif phonelist != "":
                info_sql = info_sql + """ where ttt.phone_no not in (""" + phonelist +""")"""
                #info_sql1 = info_sql1 + """ where ttt.phone_no not in ("""+phonelist+""") """
            #print info_sql
            cursor.execute(info_sql)
            user_list = cursor.fetchall()
            #cursor.execute(info_sql1)
            con.commit()
            cursor.close()
            con.close()
            if user_list:
                user_list=[ list(user) for user in user_list]
                WhiteRuleCredit()._save_mysql_it(user_list)
            else:
                print "no data insert"
        except Exception, e:
            raise e

    def save_black_data(self,user,black):
        try:
            create_time = datetime.now()
            con = cx_Oracle.connect('edw', '123com', '10.45.22.96:1521/ORCL')
            db = con.cursor()
            insert_sql = """INSERT into LC_JF_BLACKLIST(cert_no, custname, is_black, create_time) values ('%s','%s','%s','%s')""" %(user[1], user[0],black ,create_time)
            db.execute(insert_sql)
            con.commit()
            db.close()
            con.close()
        except Exception, e:
            raise e

    def _save_mysql_it(self,user_list):
    	sql_info = "insert into out_cust_source(id,name,cert_no,phone_no,sex,address,ele_product,ele_product_code,loan_limit,operate_dt,operator,data_source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_info1 = "insert into ash_out_cust_source(id,name,cert_no,phone_no) values(%s,%s,%s,%s)"
        print "start store"
        print len(user_list)
        user_list1 = [[i[0],i[1],i[2],i[3]] for i in user_list]
        con = MySQLdb.connect(host='10.27.113.75', user='bycx_bi', passwd='bycx_bi', db='bycx_bi', charset='utf8')
        cursor = con.cursor()
        # print user_list1
        cursor.executemany(sql_info1, user_list1)
        con.commit()
        cursor.close()
        con.close()

        con = MySQLdb.connect(host='10.31.133.107', user='mnguser', passwd='mnguser', db='teledb', charset='utf8')
        cursor = con.cursor()
        cursor.executemany(sql_info, user_list)
        con.commit()
        cursor.close()
        con.close()
        print "end store"


if __name__ == "__main__":

    # 启动jvm
    paths = [os.path.join(settings.BASE_DIR, "..", "jar", "nuo")]
    JvmManager.start_with_paths(paths)
    # 载入所有玖富黑名单java类
    JFBlackQueryAPI.init_load_java_class()
    WhiteRuleCredit().get_rule_data()
    JvmManager.close_jvm()
