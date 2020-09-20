#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:58:14 2019

@author: radial
"""

import pandas as pd 
import shapefile as shp
import os



def csvtoshp(t,m,label):
    '''transfer a csv file to shapefile'''
    # create a point shapefile
    output_shp = shp.Writer("/Users/radial/Public/rocket_launch/shp/{}_{}_{}.shp".format(t,m,label), shp.POINT)
    # for every record there must be a corresponding geometry.
    output_shp.autoBalance = 1
    # create the field names and data type for each.you can omit fields here
    # 顺序一定要与下面的保持一致
    output_shp.field("id_",'N')
    output_shp.field('name_num','N')
    output_shp.field('name','C',10)
    output_shp.field('latitude', 'F', 10, 8)
    output_shp.field('longitude', 'F', 10, 8)
    output_shp.field('altitude', 'F', 10, 8)
    output_shp.field('tag','N')
    output_shp.field('month','C',4)
    output_shp.field('meanrfl30', 'F', 10, 8)
    output_shp.field('meanrf', 'F', 10, 8)
    output_shp.field('cvrf', 'F', 10, 8)
    output_shp.field('mtmean', 'F', 10, 8)
    output_shp.field('mtrange', 'F', 10, 8)
    output_shp.field('Fal_PET', 'F', 10, 8)
    
    # 打开csv文件 
    data = pd.read_csv("/Users/radial/Public/rocket_launch/t_v/{}_{}_{}.csv".format(t,m,label))
    #data.columns = ['month', 'meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET',
    #               'tag', 'name_num', 'name', 'latitude', 'longitude', 'altitude']
    # 遍历写入shp文件
    if label == "t":
        for i in range(80):
            id_ = i + 1
            name_num = data['name_num'].values.tolist()[i]
            name = data['name'].values.tolist()[i]
            latitude = data['latitude'].values.tolist()[i]
            longitude = data['longitude'].values.tolist()[i]
            altitude = data['altitude'].values.tolist()[i]
            tag = data['tag'].values.tolist()[i]
            month = data['month'].values.tolist()[i]
            meanrfl30 = data['meanrfl30'].values.tolist()[i]
            meanrf = data['meanrf'].values.tolist()[i]
            cvrf = data['cvrf'].values.tolist()[i]
            mtmean = data['mtmean'].values.tolist()[i]
            mtrange = data['mtrange'].values.tolist()[i]
            Fal_PET = data['Fal_PET'].values.tolist()[i]
            # 数据写入
            output_shp.point(longitude,latitude)
            output_shp.record(id_,name_num,name,latitude,longitude,altitude,tag,month,meanrfl30, meanrf, cvrf, mtmean, mtrange, Fal_PET) # add attribute data
    if label == "v":
        for i in range(13):
            id_ = i + 1
            name_num = data['name_num'].values.tolist()[i]
            name = data['name'].values.tolist()[i]
            latitude = data['latitude'].values.tolist()[i]
            longitude = data['longitude'].values.tolist()[i]
            altitude = data['altitude'].values.tolist()[i]
            tag = data['tag'].values.tolist()[i]
            month = data['month'].values.tolist()[i]
            meanrfl30 = data['meanrfl30'].values.tolist()[i]
            meanrf = data['meanrf'].values.tolist()[i]
            cvrf = data['cvrf'].values.tolist()[i]
            mtmean = data['mtmean'].values.tolist()[i]
            mtrange = data['mtrange'].values.tolist()[i]
            Fal_PET = data['Fal_PET'].values.tolist()[i]
            # 数据写入
            output_shp.point(longitude,latitude)
            output_shp.record(id_,name_num,name,latitude,longitude,altitude,tag,month,meanrfl30, meanrf, cvrf, mtmean, mtrange, Fal_PET) # add attribute data
             
if __name__ == '__main__':
    dir='/Users/radial/Public/rocket_launch/t_v/'
    os.chdir(dir)
    for t  in  range(4):
        #for m in range(1,13):
        for m in ["sp","su","au","wi"]:
             csvtoshp(t,m,"t")
             csvtoshp(t,m,"v")
