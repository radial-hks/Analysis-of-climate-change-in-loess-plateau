#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:02:46 2019

@author: radial

"""


"""

代码目标
1、添加经纬度、高程等重要属性数据；
2、由月数据想季度数据进行转换；

"""

import pandas as pd
import os

def read_file(label,path,num):
    
    global pool
    
    # 数据读取文件
    data = pd.read_csv(path)
    
    # 春季
    row_sp = {'meanrfl30':data.loc[2:4,"meanrfl30"].sum(),
              "meanrf":data.loc[2:4,'meanrf'].mean(),
              "cvrf":data.loc[2:4,'cvrf'].mean(),
              "mtmean":data.loc[2:4,'mtmean'].mean(),
              "mtrange":data.loc[2:4,'mtrange'].mean(),
              "Fal_PET":data.loc[2:4,'Fal_PET'].sum(),
               "月":0}
    #夏季
    row_su = {'meanrfl30':data.loc[5:7,'meanrfl30'].sum(),
              "meanrf":data.loc[5:7,'meanrf'].mean(),
              "cvrf":data.loc[5:7,'cvrf'].mean(),
              "mtmean":data.loc[5:7,'mtmean'].mean(),
              "mtrange":data.loc[5:7,'mtrange'].mean(),
              "Fal_PET":data.loc[5:7,'Fal_PET'].sum(),
               "月":0}
    #秋季
    row_au = {'meanrfl30':data.loc[8:10,'meanrfl30'].sum(),
              "meanrf":data.loc[8:10,'meanrf'].mean(),
              "cvrf":data.loc[8:10,'cvrf'].mean(),
              "mtmean":data.loc[8:10,'mtmean'].mean(),
              "mtrange":data.loc[8:10,'mtrange'].mean(),
              "Fal_PET":data.loc[8:10,'Fal_PET'].sum(),
               "月":0}
    #冬季
    row_wi = {'meanrfl30':data.loc[[11,1,0],'meanrfl30'].sum(),
              "meanrf":data.loc[[11,1,0],'meanrf'].mean(),
              "cvrf":data.loc[[11,1,0],'cvrf'].mean(),
              "mtmean":data.loc[[11,1,0],'mtmean'].mean(),
              "mtrange":data.loc[[11,1,0],'mtrange'].mean(),
              "Fal_PET":data.loc[[11,1,0],'Fal_PET'].sum(),
               "月":0}
    
    data = data.append(row_sp,ignore_index = True)
    data["月"][data["月"]==0] = "sp"
    data = data.append(row_su,ignore_index = True)
    data["月"][data["月"]==0] = "su"
    data = data.append(row_au,ignore_index = True)
    data["月"][data["月"]==0] = "au"
    data = data.append(row_wi,ignore_index = True)
    data["月"][data["月"]==0] = "wi"
    # 数据添加
    data['标记位'] = label
    data["区站号"] = num
    data['台站名称'] =pool[pool["区站号"]==num]['台站名称'].values[0]
    data["纬度"] = pool[pool["区站号"]==num]['纬度'].values[0]
    data["经度"] = pool[pool["区站号"]==num]['经度'].values[0]
    data["海拔"] = pool[pool["区站号"]==num]['海拔'].values[0]
    
    med_data = data.loc[[12,13,14,15]]
    return med_data

def main():
    global pool
    global data_fal 
    # 文件读取与储存 
    lake = list()
    pool_name =pd.read_csv("/Users/radial/Public/climate/name.csv")
    for i in pool_name.values.tolist():
        for label in range(4):
            tag = int(i[0][0:5])
            path = '{}_{}.csv'.format(i[0][0:5],label)
            med = read_file(label,path,tag)
            lake.append(med)
    data_fal = pd.concat(lake,sort=False)
    for i in data_fal["月"].unique():
        for j in data_fal["标记位"].unique():
            res = data_fal[(data_fal["月"]==i)&(data_fal["标记位"]==j)]
            res.drop(['天数', '20_20', 'day_key',  'is_rain', '降水差值',
                     '日平均气温',  '温差', 'PET'],inplace=True,axis=1)
            res.to_csv("/Users/radial/Public/rocket_launch/quarter_data/{}_{}.csv".format(j,i),index=False)
    #data_fal.to_csv("data_fal.csv",index=False)  
    
    
if __name__ == '__main__':
    data_fal = pd.DataFrame()
    # 测站相关信息读取
    pool = pd.read_csv("/Users/radial/Public/climate/测站信息.csv")
    # 切换工作路径
    dir='/Users/radial/Public/rocket_launch/ex_data/'
    os.chdir(dir)
    if os.path.exists('.DS_Store'):
        os.remove(r'.DS_Store')
    main()
    

    
    