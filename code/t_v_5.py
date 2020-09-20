#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:19:14 2019

@author: radial
"""

"""
代码目标：
1、划分插值数据与验证数据 

"""

import pandas as pd
import os 

"""
#  这个函数并没有用到 
def group_data(data,t,m):
    # 数据读取
    med = data
    
    med.columns = ['month', 'meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET',
                    'tag', 'name_num', 'name', 'latitude', 'longitude', 'altitude']
    # 验证数据
    pool = [53487,53772,57083,57046,53646,53446,53602,53806,52984,52765,53705,53463,53923]
    # 测试数据
    lake_med = data['name_num'].values.tolist()
    lake = [i for i in lake_med if i not in pool]
    #  数据选取
    data_v = med[med.name_num.isin(pool)]
    data_t = med[med.name_num.isin(lake)]
    # 数据储存 
    data_v.to_csv("{}_{}_v.csv".format(t,m),index=False)
    data_t.to_csv("{}_{}_t.csv".format(t,m),index=False)

"""


if __name__ == '__main__':
    dir='/Users/radial/Public/climate/fal_data/'
    os.chdir(dir)
    for t  in  range(4):
        for m in ["sp","su","au","wi"]:
             data = pd.read_csv("/Users/radial/Public/rocket_launch/quarter_data/{}_{}.csv".format(t,m))
             #group_data(data,t,m)
             med = data
             # 平均气温
             med["meanrfl30"] = med["meanrfl30"] * 0.1
             # 平均降水
             med["meanrf"] =  med["meanrf"] * 0.1
             #  平均气温
             med["mtmean"] = med["mtmean"] * 0.1
             #  平均温差
             med["mtrange"] = med["mtrange"] * 0.1
             
             med.columns = ['month', 'meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET',
                            'tag', 'name_num', 'name', 'latitude', 'longitude', 'altitude']
             # 验证数据
             #pool = [53478,53772,53975,53543,53754,53942,53519,53821,52996,53705,53915,52787,52984]
             pool = [53478,53772,53975,53543,53754,53942,53519,53821,52996,53705,53915,52866,52984]
             # 测试数据
             lake_med = data['name_num'].values.tolist()
             lake = [i for i in lake_med if i not in pool]
             #  数据选取
             data_v = med[med.name_num.isin(pool)]
             data_t = med[med.name_num.isin(lake)]
             # 数据储存 
             data_v.to_csv("/Users/radial/Public/rocket_launch/t_v/{}_{}_v.csv".format(t,m),index=False)
             data_t.to_csv("/Users/radial/Public/rocket_launch/t_v/{}_{}_t.csv".format(t,m),index=False)