#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:19:10 2019

@author: radial
"""

import  pandas as pd 
import numpy as np

# 读取数据
data = pd.read_csv("/Users/radial/Public/rocket_launch/htgy_2017.csv")

# 读取建站时间

res =data[['区站号','年']].groupby(['区站号']).min()
res["区站号"]  =  res.index
res["cr"] =  2019 -  res["年"]

pool={"纬度":[],"经度":[],"高程":[]}

for i in res["区站号"].values:
    med_one = data[data["区站号"]== i]["纬度"].unique().max()
    pool["纬度"].append(med_one//100 + med_one % 100 / 60)
    
    med_two = data[data["区站号"]== i]["经度"].unique().max()
    pool["经度"].append(med_two//100 + med_two % 100 / 60)
    
    med_three = data[data["区站号"]== i]["高程"].unique().max()/10
    pool["高程"].append(med_three)
    
med_data = pd.DataFrame(pool,index = res["区站号"].values)

# 写入最终的数据 
fal = pd.concat([res,med_data],axis=1)
fal.to_csv("/Users/radial/Public/rocket_launch/name_id.csv")

def  year(fal):
    j = 10
    for i in range(4):
        med = fal["年"][(fal["年"]>1950)&(fal["年"]<(1950+j))].count()
        print("{}至{}年起共计{}个测站".format(1950,1950+j,med))
        j += 10
year(fal)


ee =data[['区站号','年']].groupby(['区站号']).max()




import pandas as pd 
import shapefile as shp
import os

def csvtoshp():
    global  fal  
    '''transfer a csv file to shapefile'''
    # create a point shapefile
    output_shp = shp.Writer("/Users/radial/Public/rocket_launch/htgy_2017.shp", shp.POINT)
    # for every record there must be a corresponding geometry.
    output_shp.autoBalance = 1
    # create the field names and data type for each.you can omit fields here
    # 顺序一定要与下面的保持一致
    output_shp.field("id_",'N')
    output_shp.field('name_num','N')
    output_shp.field('latitude', 'F', 10, 8)
    output_shp.field('longitude', 'F', 10, 8)
    output_shp.field('altitude', 'F', 10, 8)
    output_shp.field('tag','N')
    for i in range(142):
        id_ = i+1
        name_num = fal['区站号'].values.tolist()[i]
        latitude = fal['纬度'].values.tolist()[i]
        longitude = fal['经度'].values.tolist()[i]
        altitude = fal['高程'].values.tolist()[i]
        tag = fal['cr'].values.tolist()[i]
        # 数据写入
        output_shp.point(longitude,latitude)
        output_shp.record(id_,name_num,latitude,longitude,altitude,tag) # add attribute data

csvtoshp() 