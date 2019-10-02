#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:23:10 2019

@author: radial
"""

### 我是气温分隔符

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/TEM")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
data["日平均气温"]=data["all"].str[35:41]
data["日最高气温"]=data["all"].str[42:48]
data["日最低气温"]=data["all"].str[49:55]
# data["k1"]=data["all"].str[56]
# data["k2"]=data["all"].str[58]
# data["k3"]=data["all"].str[60]

del  data['all']

data.to_csv("/Users/radial/Public/climate/totem.csv",index=0)


###  我是降水分隔符

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/PRE")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
# data["20_8"]=data["all"].str[35:41]
# data["8_20"]=data["all"].str[42:48]
data["20_20"]=data["all"].str[49:55]
# data["k1"]=data["all"].str[56]
# data["k2"]=data["all"].str[58]
# data["k3"]=data["all"].str[60]

del  data['all']

data.to_csv("/Users/radial/Public/climate/topre.csv",index=0)


### 我是湿度分隔符

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/RHU")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
data["平均相对湿度"]=data["all"].str[35:41]
data["最小相对湿度"]=data["all"].str[42:48]
#data["20_20"]=data["all"].str[49:55]
# data["k1"]=data["all"].str[56]
# data["k2"]=data["all"].str[58]
# data["k3"]=data["all"].str[60]

del  data['all']

data.to_csv("/Users/radial/Public/climate/torhu.csv",index=0)


### 我是气压分割符号

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/PRS")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
data["日平均气压"]=data["all"].str[35:41]
data["日最高气压"]=data["all"].str[42:48]
data["日最低气压"]=data["all"].str[49:55]
# data["k1"]=data["all"].str[56]
# data["k2"]=data["all"].str[58]
# data["k3"]=data["all"].str[60]

del  data['all']

data.to_csv("/Users/radial/Public/climate/toprs.csv",index=0)


### 我是风速分隔符

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/WIN")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
data["平均风速"]=data["all"].str[35:41]
data["最大风速度"]=data["all"].str[42:48]
data["最大风速风向"]=data["all"].str[49:55]
data["极大风速度"]=data["all"].str[56:62]
data["极大风速风向"]=data["all"].str[63:69]


del  data['all']

data.to_csv("/Users/radial/Public/climate/towin.csv",index=0)

###  我是日照分隔符

import pandas as pd 
# data=pd.read_csv("TEM.csv",sep="",header=["区站号","经度","纬度","高程","年","月","日","平均气温","日最高气温","日最低气温","平","高","低"])
data=pd.read_csv("/Users/radial/Public/climate/SSD")

data.columns=["all"]

data["区站号"]=data["all"].str[0:5]
data["纬度"]=data["all"].str[6:10]
data["经度"]=data["all"].str[11:16]
data["高程"]=data["all"].str[17:23]
data["年"]=data["all"].str[24:28]
data["月"]=data["all"].str[29:31]
data["日"]=data["all"].str[32:34]
data["日照时数"]=data["all"].str[35:41]
#data["最大风速度"]=data["all"].str[42:48]
#data["最大风速风向"]=data["all"].str[49:55]
#data["极大风速度"]=data["all"].str[56:62]
#data["极大风速风向"]=data["all"].str[63:69]


del  data['all']

data.to_csv("/Users/radial/Public/climate/tossd.csv",index=0)