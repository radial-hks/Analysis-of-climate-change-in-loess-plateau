# 气候变化特征

import pandas as pd 
import numpy as np 
import os 


## 数据读取与拆分
def read_file(path):
    ## 数据读取
    data = path
    data["is_rain"] = 0 
    data["day_key"] = 1
    data["is_rain"][data["20_20"]>0] = 1
    data["温差"] =  data["日最高气温"] - data["日最低气温"]

    # 研究区时间划分1980~1989、1990~1999、2000~2009、2010~2017
    data_1980 = data[(data["年"]>1979)&(data["年"]<1990)]
    data_1990 = data[(data["年"]>1989)&(data["年"]<2000)]
    data_2000 = data[(data["年"]>1999)&(data["年"]<2010)]
    data_2010 = data[(data["年"]>2009)&(data["年"]<2018)]
    
    # 读取数据返回 
    filepool = [data_1980,data_1990,data_2000,data_2010]
    return  filepool
    

## 特征提取函数
# 1、月总降水量：meanrfl30
def  meanrl30(matrix):
    global res
    res["20_20"] =  matrix[["月","20_20"]].groupby(["月"]).sum().reset_index()["20_20"]
    res["day_key"] =  matrix[["月","day_key"]].groupby(["月"]).sum().reset_index()["day_key"]
    res["meanrfl30"] =  res["20_20"]/res["day_key"]*res["天数"]

# 2、降雨天数平均降雨量：meanrf 

def  meanrf(matrix):
    global res
    res["is_rain"] =  matrix[["月","is_rain"]].groupby(["月"]).sum().reset_index()["is_rain"]
    res["meanrf"] = res["20_20"]/res["is_rain"]

# 3、降水天数降水变异系数 
def cvrf(matrix):
    global res
    matrix["降水差值"] = 0
    for month in range(1,13):
        matrix["降水差值"][(matrix['月']==month)&(matrix['is_rain']==1)]= matrix["20_20"][(matrix['月']==month)&(matrix['is_rain']==1)] - res["meanrf"][res['月']==month].values[0]
    matrix["降水差值"]= np.square(matrix["降水差值"])
    res["降水差值"] = matrix[["降水差值","月"]].groupby(["月"]).sum().reset_index()["降水差值"]
    res["cvrf"] =  np.sqrt(res["降水差值"]/res["is_rain"])/res["meanrf"]
    
# 4、月平均气温 
"""
j: 代表研究时间的总月数
"""
def mtmean(matrix,j):
    global res
    res["日平均气温"] =  matrix[["月","日平均气温"]].groupby(["月"]).sum().reset_index()["日平均气温"]
    res["mtmean"] =  res["日平均气温"]/j

# 5、月平均温差 
def  mtrange(matrix):
    global res
    res["温差"] =  matrix[["月","温差"]].groupby(["月"]).sum().reset_index()["温差"]
    res["mtrange"] =  res["温差"]/j


# 6、月蒸发量
def evaporation_cap(matrix,j,number):
    global res
    global pool 
    # 站点数据读取
    data = matrix

    """
    实验数据输入及预处理
    """
    med = data[['年', '月','日平均气温', '平均相对湿度','平均风速', '日照时数']].groupby(['年','月'],as_index= False).mean()
    med_one= data[['年', '月','日照时数']].groupby(['年','月'],as_index= False).sum()
    med_two= data[['年', '月','日最高气温']].groupby(['年','月'],as_index= False).max()
    med_three= data[['年', '月','日最低气温']].groupby(['年','月'],as_index= False).min()

    med["日照时数"] = med_one["日照时数"]
    med['日最高气温'] = med_two['日最高气温']/10
    med['日最低气温'] = med_three['日最低气温']/10
    
    med["纬度"] = pool[pool["区站号"]==number]['纬度'].values[0]
    med["海拔"] = pool[pool["区站号"]==number]['海拔'].values[0]
    
    # 数据转换为标准计算输入单位
    med["日平均气温"] = med["日平均气温"]/10
    

    # 计算某月15号是一年中第几天？？？及添加每月的时间时间
    med['day_in_year']=0
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
    
    #  GroupBy 聚合归类函数
    res["PET"] = med[["月","ET0"]].groupby(["月"]).sum().reset_index()["ET0"]
    res["Fal_PET"] = res["PET"]/j
    
    
    
def main():
    global j
    global res
    global pool 
    #  切换工作路径
    dir='/Users/radial/Public/rocket_launch/research_data'
    os.chdir(dir)
    if os.path.exists('.DS_Store'):
        os.remove(r'.DS_Store')
    # 依次读取文件数据
    for name in os.listdir():
        # 提取文件名称信息
        title = name[:5]
        print(title)
        number = int(name[:5])
        #tag = 0
        
        # 节点数据读取
        data_node = pd.read_csv(name)
        
        # 降水数据修正(毕设中出现的最大的问题)
        #data_node.replace(37266,0)
        
        # 异常值与特定含义值处理
        data_node['日平均气温'][data_node['日平均气温']==32766] = data_node[data_node['日平均气温']!=32766].mean()
        data_node['日最高气温'][data_node['日最高气温']==32766] = data_node[data_node['日最高气温']!=32766].mean()
        data_node['日最低气温'][data_node['日最低气温']==32766] = data_node[data_node['日最低气温']!=32766].mean()
        data_node['平均相对湿度'][data_node['平均相对湿度']==32766] = data_node[data_node['平均相对湿度']!=32766].mean()
        data_node['平均风速'][data_node['平均风速']==32766] = data_node[data_node['平均风速']!=32766].mean()
        data_node['20_20'][data_node['20_20']==32766] = data_node[data_node['20_20']!=32766].mean()
        data_node['日照时数'][data_node['日照时数']==32766] = data_node[data_node['日照时数']!=32766].mean()
        # 降雨异常处理
        data_node['20_20'][data_node['20_20']==32700] = 0
        data_node['20_20'][(data_node['20_20']>30000)&(data_node['20_20']<31000)] = data_node['20_20'][(data_node['20_20']>30000)&(data_node['20_20']<31000)]//30000 
        data_node['20_20'][(data_node['20_20']>31000)&(data_node['20_20']<32000)] = data_node['20_20'][(data_node['20_20']>31000)&(data_node['20_20']<32000)]//31000
        data_node['20_20'][(data_node['20_20']>32000)&(data_node['20_20']<33000)] = data_node['20_20'][(data_node['20_20']>32000)&(data_node['20_20']<33000)]//32000
        
        
        tag = 0 
        for i in read_file(data_node):
            if  tag > 2:
                j = 120
            else:
                j = 96
            #data = i
            # groupby 数据初始化
            dic =  {"月":[1,2,3,4,5,6,7,8,9,10,11,12],
                    "天数":[31,28,31,30,31,30,31,31,30,31,30,31]}
            res = pd.DataFrame(dic)
            
            # 1、月总降水量
            meanrl30(i)
            # 2、降雨天数平均降水量
            meanrf(i)
            # 3、降雨天数降雨量变异系数
            cvrf(i)
            # 4、月平均温度
            mtmean(i,j)
            # 5、月平均温差
            mtrange(i)
            # 6、月总蒸发量 
            evaporation_cap(i,j,number)
            #res.astype(np.int64,copy=True)
            # 数据保存
            res.to_csv("/Users/radial/Public/rocket_launch/ex_data/"+title+"_"+str(tag)+".csv",index=False)
            tag += 1

if __name__ == '__main__':
    # 测站相关信息读取
    pool = pd.read_csv("/Users/radial/Public/climate/测站信息.csv")
    # groupby 数据初始化
    dic =  {"月":[1,2,3,4,5,6,7,8,9,10,11,12],
            "天数":[31,28,31,30,31,30,31,31,30,31,30,31]}
    j = 0
    res = pd.DataFrame(dic)
    main()
