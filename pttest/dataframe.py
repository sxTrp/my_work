# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

all_list = [[1,2,3,4],[4,3,2,1],[4,5,6,7],[2,3,4,5]]

a=[]
af = pd.DataFrame(all_list,columns=["phone","phone2","phone3","phone4"])
for i in af.values:
    print i
# parents_cell = af["phone"][af["phone2"].isin([2,3])]
# print parents_cell
# print af[af['phone3'].isin(list(parents_cell))]
# print af[af['phone3'].isin(parents_cell)]
# print sum([True,True,True,False])