#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:20:35 2019

@author: radial
"""
import shapefile as shp
import pandas as pd
import  numpy as np



path = r"/Users/radial/Public/rocket_launch/topoint/"
title ="0_sp_cvrf.shp"


dic = {'meanrfl30':[], 'meanrf':[], 'cvrf':[], 'mtmean':[], 'mtrange':[], 'Fal_PET':[],
       'meanrfl30_v':[], 'meanrf_v':[], 'cvrf_v':[], 'mtmean_v':[], 'mtrange_v':[], 'Fal_PET_v':[]}


pool = ['meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET']
for  name in pool:
    lake_one = list()
    lake_two = list()
    i = pool.index(name)+8
    for t in range(4):
        for m in  ["sp","su","au","wi"]:
            title = "{}_{}_{}.shp".format(t,m,name)
            for j in shp.Reader(path+title).records():
                lake_one.append(j[i])
                lake_two.append(j[-1])
    dic[name] = lake_one
    dic[name+"_v"] = lake_two
    
data = pd.DataFrame(dic)
data.to_csv("/Users/radial/Public/rocket_launch/topoint/data_v.csv",index=False)


def nse(data,name):
    data["med_one"] = data[name] - data[name+"_v"]
    data["med_two"] = data[name] - np.mean(data[name+"_v"])
    res_one = 1 - np.sum(np.square(data["med_one"]))/ np.sum(np.square(data["med_two"]))
    res_two = np.sqrt(np.sum(np.square(data["med_one"]))/208)
    return res_one,res_two

pool = ['meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET']
for i in pool:
    print(i,nse(data,i))     