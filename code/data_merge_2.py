import  pandas as pd 

### 我是气温分隔符
tem = pd.read_csv("/Users/radial/Public/climate/totem.csv")

###  我是降水分隔符
pre = pd.read_csv("/Users/radial/Public/climate/topre.csv")

### 我是湿度分隔符
rhu = pd.read_csv("/Users/radial/Public/climate/torhu.csv")

### 我是气压分割符号
prs = pd.read_csv("/Users/radial/Public/climate/toprs.csv")

### 我是风速分隔符
win = pd.read_csv("/Users/radial/Public/climate/towin.csv")

###  我是日照分隔符
ssd = pd.to_csv("/Users/radial/Public/climate/tossd.csv")


##  数据合并及保存
tem_pre = pd.merge(tem,pre,how="left",on=["区站号","经度","纬度","高程","年","月","日"])
rhu_prs = pd.merge(rhu,prs,how="left",on=["区站号","经度","纬度","高程","年","月","日"])
win_ssd = pd.merge(win,ssd,how="left",on=["区站号","经度","纬度","高程","年","月","日"])


_second = pd.merge(tem_pre,rhu_prs,how="left",on=["区站号","经度","纬度","高程","年","月","日"])
res =  pd.merge(_second,win_ssd,how="left",on=["区站号","经度","纬度","高程","年","月","日"])

res.to_csv("/Users/radial/Public/climate/toall.csv",index=0)


###   提取研究区域数据

all = pd.read_csv("/Users/radial/Public/rocket_launch/toall.csv")
htgy = all[
        (all["纬度"]>33)&
        (all["纬度"]<42)&
        (all["经度"]<115)&
        (all["经度"]>100)]

htgy.to_csv("/Users/radial/Public/rocket_launch/htgy.csv",index=0)



###   提取研究测站数据
lake_drop = []
lake_add = []
for  i in  htgy["区站号"].unique():
    pool = htgy[htgy["区站号"]==i]["年"].unique()
    if min(pool) >  1981:
        lake_drop.apped(i)
        pass
    else:
        lake_add.append(i)
        htgy[htgy["区站号"]==i].to_csv('/Users/radial/Public/climate'+str(i)+".csv",index=0)




#  补充1980年数据  

new_one = pd.read_csv("/Users/radial/Public/rocket_launch/new_one.csv")


lake = list()
for i in  htgy["区站号"].unique():
    if  i  in new_one["区站号"].unique():
            if  new_one[new_one["区站号"]==i][new_one["年"]==1980].shape[0]>0:
                lake.append(i)
                res = pd.concat([htgy[htgy["区站号"]==i],new_one[new_one["区站号"]==i][new_one["年"]==1980]],sort=False)
                res.to_csv("/Users/radial/Public/climate/research_now/"+str(i)+".csv",index=0)



# 为简单了事，数据匹配错误
# 修正方案
#new_one = pd.read_csv("/Users/radial/Public/climate/new_one.csv")
                
new_one = pd.read_csv("/Users/radial/Public/rocket_launch/new_one.csv")
htgy = pd.read_csv("/Users/radial/Public/rocket_launch/htgy.csv") 

new_one.columns=['区站号', '年', '月', '日', '平均本站气压', '日最高本站气压', '日最低本站气压',
       '日平均气温', '日最高气温', '日最低气温', '平均相对湿度', '最小相对湿度', '20_20',
       '平均风速', '最大风速', '最大风速的风向', '极大风速', '极大风速的风向',
       '日照时数']

lake = list()
for i in  htgy["区站号"].unique():
    if  i  in new_one["区站号"].unique():
            if  new_one[new_one["区站号"]==i][new_one["年"]==1980].shape[0]>0:
                lake.append(i)
                hy= htgy[htgy["区站号"]==i][['区站号', '年', '月', '日', '日平均气温', '日最高气温', '日最低气温',
       '20_20', '平均相对湿度', '平均风速', '日照时数']]
                new = new_one[new_one["区站号"]==i][new_one["年"]==1980][['区站号', '年', '月', '日', '日平均气温', '日最高气温', '日最低气温',
       '20_20', '平均相对湿度', '平均风速', '日照时数']]
                res = pd.concat([hy,new],sort=False)
                res.to_csv("/Users/radial/Public/rocket_launch/"+str(i)+".csv",index=0)