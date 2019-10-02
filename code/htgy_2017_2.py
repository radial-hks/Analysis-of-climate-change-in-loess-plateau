#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:37:54 2019

@author: radial
"""

import  pandas as pd 
import numpy as np


"""
一 、数据清洗及站点存储

"""

# 数据读取 
data = pd.read_csv("/Users/radial/Public/rocket_launch/htgy_2017.csv")

# 数据清洗 
# 异常值与特定含义值处理
data['日平均气温'][data['日平均气温']==32766] = data[data['日平均气温']!=32766].mean()
data['日最高气温'][data['日最高气温']==32766] = data[data['日最高气温']!=32766].mean()
data['日最低气温'][data['日最低气温']==32766] = data[data['日最低气温']!=32766].mean()
data['平均相对湿度'][data['平均相对湿度']==32766] = data[data['平均相对湿度']!=32766].mean()
data['平均风速'][data['平均风速']==32766] = data[data['平均风速']!=32766].mean()
data['20_20'][data['20_20']==32766] = data[data['20_20']!=32766].mean()
data['日照时数'][data['日照时数']==32766] = data[data['日照时数']!=32766].mean()

# 降雨异常处理
data['20_20'][data['20_20']==32700] = 0
data['20_20'][(data['20_20']>30000)&(data['20_20']<31000)] = data['20_20'][(data['20_20']>30000)&(data['20_20']<31000)]//30000 
data['20_20'][(data['20_20']>31000)&(data['20_20']<32000)] = data['20_20'][(data['20_20']>31000)&(data['20_20']<32000)]//31000
data['20_20'][(data['20_20']>32000)&(data['20_20']<33000)] = data['20_20'][(data['20_20']>32000)&(data['20_20']<33000)]//32000

# 中间数据值计算 
data["is_rain"] = 0 
data["day_key"] = 1
data["is_rain"][data["20_20"]>0] = 1
data["温差"] =  data["日最高气温"] - data["日最低气温"]

# 分站点信息存储
med = pd.DataFrame(data["区站号"].unique())
med.to_csv("/Users/radial/Public/rocket/id.csv",index = False)
for i in data["区站号"].unique():
    res = data[data["区站号"]==i]
    #res.reset_index()
    #res["纬度"] = res["纬度"][0]
    #res["经度"] = res["经度"][0]
    #res["高程"] = res["高程"][0]
    res.to_csv("/Users/radial/Public/rocket/{}.csv".format(str(i)),index = False)


"""
二 、数据特征提取

"""


# 数据特征提取

# 1、月总降水量：meanrfl30
 
def  meanrl30(matrix):
    global res
    res = matrix[['年',"月","20_20"]].groupby(['年',"月"]).sum()
    #res["day_key"] =  matrix[['年',"月","day_key"]].groupby(['年',"月"]).sum().reset_index()["day_key"]
    res["id"] =res.index
    res["年"] = pd.DataFrame([i[0] for i in res["id"]],index=res.index)
    res["月"] = pd.DataFrame([i[1] for i in res["id"]],index=res.index)  
    res["meanrfl30"] = res["20_20"]
    res.fillna(0,inplace=True)

# 2、降雨天数平均降雨量：meanrf 

def  meanrf(matrix):
    global res
    res["is_rain"] =  matrix[['年',"月","is_rain"]].groupby(['年',"月"]).sum()["is_rain"]
    res["meanrf"] = res["20_20"]/res["is_rain"]
    res.fillna(0,inplace=True)

def cvrf(matrix):
    global res
    matrix["降水差值"] = 0
    for year in matrix["年"]:
        for month in range(1,13):
            matrix["降水差值"][(matrix['年']==year)&(matrix['月']==month)&(matrix['is_rain']==1)]= matrix["20_20"][(matrix['年']==year)&(matrix['月']==month)&(matrix['is_rain']==1)] - res["meanrf"][(res['年']==year)&(res['月']==month)].values[0]
    matrix["降水差值"]= np.square(matrix["降水差值"])
    res["降水差值"] = matrix[["降水差值",'年',"月"]].groupby(['年',"月"]).sum()["降水差值"]
    res["cvrf"] =  np.sqrt(res["降水差值"]/res["is_rain"])/res["meanrf"]
    res.fillna(0,inplace=True)
    
# 4、月平均气温 

"""
j: 代表研究时间的总月数
"""
def mtmean(matrix):
    global res
    res["day_key"] = matrix[['年',"月","day_key"]].groupby(['年',"月"]).sum()["day_key"]
    res["日平均气温"] =  matrix[['年',"月","日平均气温"]].groupby(['年',"月"]).mean()["日平均气温"]
    res["mtmean"] =  res["日平均气温"]/res["day_key"]

# 5、月平均温差 

def  mtrange(matrix):
    global res
    res["温差"] =  matrix[['年',"月","温差"]].groupby(['年',"月"]).mean()["温差"]
    res["mtrange"] =  res["温差"]/res["day_key"]

# 6、月蒸发量

def evaporation_cap(matrix,number):
    global res
    global pool 
    # 站点数据读取
    data = matrix

    """
    实验数据输入及预处理
    """
    med = data[['年', '月','日平均气温', '平均相对湿度','平均风速', '日照时数']].groupby(['年','月']).mean()
    med["id"] =med.index
    med["年"] = pd.DataFrame([i[0] for i in med["id"]],index=med.index)
    med["月"] = pd.DataFrame([i[1] for i in med["id"]],index=med.index) 
    med_one= data[['年', '月','日照时数']].groupby(['年','月']).sum()
    med_two= data[['年', '月','日最高气温']].groupby(['年','月']).max()
    med_three= data[['年', '月','日最低气温']].groupby(['年','月']).min()

    med["日照时数"] = med_one["日照时数"]
    med['日最高气温'] = med_two['日最高气温']/10
    med['日最低气温'] = med_three['日最低气温']/10
    
    med["纬度"] = pool[pool["区站号"]==number]['纬度'].values[0]
    med["海拔"] = pool[pool["区站号"]==number]['海拔'].values[0]
    med["经度"] = pool[pool["区站号"]==number]['经度'].values[0]
    
    # 数据转换为标准计算输入单位
    med["日平均气温"] = med["日平均气温"]/10
    
    # 计算某月15号是一年中第几天？？？及添加每月的时间时间
    med['day_in_year'] = 0
    med["month_days"] = 0 
    month_days=[30,28,31,30,31,30,31,31,30,31,30,31]
    day_in_year = [15,46,76,106,137,167,198,228,259,289,319,350]
    for i in  range(12):
        j=i+1
        med["day_in_year"][med["月"]==j] = day_in_year[i]
        med["month_days"][med["月"]==j] = month_days[i]
    
    """
    1、分步进行特征提取
    
    """
    # 使用最高温度与最低温度计算AE值
    med["med_1_AE"] = 0.6108 * np.exp(np.true_divide(med["日最高气温"]*17.27,med["日最高气温"]+237.3))
    med["med_2_AE"] = 0.6108 * np.exp(np.true_divide(med["日最低气温"]*17.27,med["日最低气温"]+237.3))
    med["AE"] = np.true_divide(med["med_1_AE"]+med["med_2_AE"],2)
    
    # 使用相对湿度计算AF值
    med["AF"] = np.true_divide(med["AE"]* med["平均相对湿度"],100)
    
    # 使用平均风速计算J值(修正值)
    med["J"] = np.true_divide(med["平均风速"] * 0.1 * 4.87,np.log10(67.8 * 10-5.42))
    
    
    # 使用海拔、平均温度计算Y值
    med["med_3_Y"] = (med["日平均气温"]+np.true_divide(0.665*med["海拔"], 1000))**(1+0.34 * med["J"])
    ## 严重错误标注
    #med["med_1_Y"] = 101.3 * np.power(np.true_divide(293-0.0065*med["med_3_Y"],293),5.26)
    med["med_1_Y"] = 101.3 * np.power(np.true_divide(293-0.0065*med["海拔"],293),5.26)
    ## 严重错误标注
    #med["med_2_Y"] = np.true_divide(np.true_divide(0.618 * np.exp(17.27 * med["日平均气温"]),med["日平均气温"]+237.3),np.power(med["日平均气温"]+237.3,2)) * 4096
    med["med_2_Y"] = np.true_divide(0.618 * np.exp(np.true_divide(17.27 * med["日平均气温"],med["日平均气温"]+237.3)),np.power(med["日平均气温"]+237.3,2)) * 4096
    med["med_4_Y"] =  (med["med_2_Y"] +0.665*0.001 * med["med_1_Y"]) * (1+ 0.34 * med["J"]) 
    med["Y"] = np.true_divide((0.665* 0.001 * med["med_1_Y"]),med["med_4_Y"])
    
    
    #  使用W，V，J数据计算X值
    med["X"] = np.true_divide(med["med_2_Y"],med["med_2_Y"]+(0.665*0.001*med["med_1_Y"])*(1+(0.34*med["J"])))
    
    
    # 使用日照时间计算AA值 
    med["M"] = np.true_divide(med["日照时数"],med["month_days"])*0.1
    
    med["Q"] = np.true_divide(np.pi * med["纬度"],180)
    med["R"] = 0.409 * np.sin(2*np.pi*med["day_in_year"]/365-1.39)
    med["S"] = np.arccos(-np.tan(med["Q"]*np.tan(med["R"])))
    med["T"] = 24 * med["S"]/ np.pi
    
    med["U"] =1+0.033*np.cos(2*np.pi*med["day_in_year"]/365)
    med["Z"]=  24*60*0.082*med["U"]*(med["S"]*np.sin(med["Q"])*np.sin(med["R"])+np.cos(med["Q"])*np.cos(med["R"]*np.sin(med["S"])))/np.pi
    
    med["AA"] = (0.22+0.55*med["M"]/med["T"])*med["Z"]
    
    med["AB"] = (0.75 +2 * 0.00001 * med["海拔"])* med["Z"]
    med["AC"] =  med["AA"]/med["AB"]*med["AA"]
    
    # 计算AG值
    med["AD"] = 0.000000004903*(np.power(med["日最高气温"]+273.16,4)+ np.power(med["日最低气温"]+273.16,4))*0.5
    med["AF"] = med["平均相对湿度"]*med["AE"]*0.01
    med["AG"] =  med["AD"] * (0.34-0.14* np.sqrt(med["AF"]))*(1.35*med["AA"]/med["AB"]-0.35)
    
    
    # 计算ET
    med["日平均气温_"]= med["日平均气温"].shift(1)
    med["日平均气温_"].iloc[0]= med["日平均气温"].iloc[12]
    med["ET"] = (med["AE"]-med["AF"])*med["Y"]*900*med["J"]/(med["日平均气温"]+273)+((med["AC"]-med["AG"])-(med["日平均气温"]-med["日平均气温_"])*0.14)*0.408*med["X"]
    med["ET0"] =  med["ET"] * med['month_days']
    
    res["pet"] = med["ET0"]
    #  GroupBy 聚合归类函数
    #res["PET"] = med[["月","ET0"]].groupby(["月"]).sum().reset_index()["ET0"]
    #res["Fal_PET"] = res["PET"]/j


def main(y):
#for y in a.values:
    print(y[0])
    med_data = pd.read_csv(r"D:/radial/data/rocket/{}.csv".format(str(y[0])))
    # 1、月总降水量
    meanrl30(med_data)
    # 2、降雨天数平均降水量
    meanrf(med_data)
    # 3、降雨天数降雨量变异系数
    cvrf(med_data)
    # 4、月平均温度
    mtmean(med_data)
    # 5、月平均温差
    mtrange(med_data)
    # 6、月总蒸发量 
    evaporation_cap(med_data,y[0])
    #res.astype(np.int64,copy=True)
    # 数据保存
    res.to_csv(r"D:/radial/data/ex_data/{}.csv".format(str(y[0])),index=False)



# 测站相关信息读取
a = pd.read_csv(r"D:/radial/id.csv")
pool = pd.read_csv(r"D:/radial/data/测站信息.csv")

freeze_support()
lake = Pool(10)

for y in a.values:
    #pool.apply_async(func=main,args=(y,))
    lake.apply_async(func=main,args=(y))

print('end')
lake.close()
lake.join()
