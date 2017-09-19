import os

def prt(line):
    print line

def fil(p):
    if p%3==0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    al = [x ** 2 for x in range(9)]
    # # test 1
    # lts_path = os.path.join('E:', 'lts.txt')
    # with open(lts_path) as lts_file:
    #     lines = lts_file.readlines()
    #
    #     alr =[prt(line) for line in lines]
    x = ("2016-01-01","2016-02-07","2016-02-08","2016-02-09","2016-02-10","2016-02-11",
     "2016-02-12","2016-02-13","2016-04-04","2016-05-01","2016-06-09","2016-06-10",
     "2016-06-11","2016-09-15","2016-09-16","2016-09-17","2016-10-01","2016-10-02",
     "2016-10-03","2016-10-04","2016-10-05","2016-10-06","2016-10-07",
     "2017-01-01","2017-01-27","2017-01-28","2017-01-29","2017-01-30","2017-01-31",
     "2017-02-01","2017-02-02","2017-04-02","2017-04-03","2017-04-04","2017-05-01",
     "2017-05-28","2017-05-29","2017-05-30","2017-10-01","2017-10-02",
     "2017-10-03","2017-10-04","2017-10-05","2017-10-06","2017-10-07")
    from datetime import datetime
    from business_calendar import Calendar, MO, TU, WE, TH, FR
    cal = Calendar()
    t = datetime.strptime("2016-04-04 15:46:20", "%Y-%m-%d %H:%M:%S")
    print t.date()
    print str(t.date()) in x
    # date1 = datetime.strptime("2016-10-28 15:46:20", "%Y-%m-%d %H:%M:%S")
    # print cal.busdaycount(date1, date2)

    # import holidays
    #
    # us_holidays = holidays.US() # or holidays.US()
    #
    # print t in us_holidays  # True
    # -*- coding:utf-8 -*-


