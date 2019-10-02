import arcpy
from arcpy.sa import *

# 设置工作环境
arcpy.env.workspace = "D:/lp_data"
pool = ['meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET']


"""
1、点文件预处理（定义地理坐标系与重新投影）

"""

#  首先设定一个手动完成的参考shp文件
#  然后跳过循环设定
dsc = arcpy.Describe(r"D:/lp_data/source/0_sp_t.shp")
coord_sys = dsc.spatialReference

#  添加地理坐标系
for t  in  range(4):
    for m in ["sp","su","au","wi"]:
        for tag in ["t","v"]:
            if t==0 and m == "sp" and tag == "t":
                pass
            else:
                in_dataset = "D:/lp_data/source/{}_{}_{}.shp".format(t,m,tag)
                arcpy.DefineProjection_management(in_dataset, coord_sys)



# 投影转换
for t  in  range(4):
    for m in ["sp","su","au","wi"]:
        for tag in ["t","v"]:
            input_features = "D:/lp_data/source/{}_{}_{}.shp".format(t,m,tag)
            outCS = arcpy.SpatialReference("D:/lp_data/project/WGS_1984_Albers.prj")
            outfc = "D:/lp_data/project_data/{}_{}_{}.shp".format(t,m,tag)
            arcpy.Project_management(input_features, outfc, outCS)



"""
克里金插值（废弃）
"""
# 克里金插值
for t  in  range(4):
    for m in ["sp","su","au","wi"]:
        for tag in ["t","v"]:
            for  index in  pool:
                if  tag == 't':
                    # input_features = "{}_{}_{}_p.shp".format(t,m,tag)
                    input_features = "{}_{}_t_p.shp".format("0", "1")
                    # Set local variables
                    #inFeatures = "{}_{}_t_p.shp".format("0", "1")
                    field = "mtmean"
                    cellSize = 4000
                    outVarRaster = "{}_{}_{}_{}".format(t,m,tag,index)
                    outVarRaster = "{}_{}_t_{}".format("0", "1", "mtmaean")
                    lagSize = 2000
                    majorRange = 2.6
                    partialSill = 542
                    nugget = 0
                    # Set complex variables
                    kModelOrdinary = KrigingModelOrdinary("CIRCULAR", lagSize,
                                majorRange, partialSill, nugget)
                    kRadius = RadiusFixed(20000, 1)
                    # Execute Kriging
                    outKriging = Kriging(inFeatures, field, kModelOrdinary, cellSize,
                                kRadius, outVarRaster)
                    outKriging.save("{}_{}_{}_{}.shp".format(t,m,tag,index)
                    outKriging.save("{}_{}_t_{}.shp".format("0", "1", "mtmaean")
                if tag == 'v':
                    pass
                    # valField = index
                    # input_features = "{}_{}_{}_p.shp".format(t,m,tag)
                    # outRaster = "{}_{}_{}_{}".format(t,m,tag,index)
                    # assignmentType = "MAXIMUM"
                    # priorityField = ""
                    # cellSize = 2000
                    # # Execute PointToRaster
                    # arcpy.PointToRaster_conversion(inFeatures, valField, outRaster,
                    #             assignmentType, priorityField, cellSize)



"""
2、克里金插值

"""

import arcpy
from arcpy.sa import *

# 设置工作环境
arcpy.env.workspace = "D:/lp_data"

# 真正的克里金插值在这里啊
pool = [ 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET','meanrfl30']
#pool = ['meanrfl30']
for t  in  range(4):
    for m in ["sp","su","au","wi"]:
        for name in  pool:
            outKrig = Kriging("D:/lp_data/project_data/{}_{}_t.shp".format(t,m), name, KrigingModelOrdinary("CIRCULAR", 2000, 2.6, 542, 0), 1000, RadiusFixed(20000, 12))
            if  name == 'meanrfl30':
                title = "{}_{}_{}".format("mf30", t, m)
            else :
                title = "{}_{}_{}".format(name, t, m)
            outKrig.save(r"D:/lp_data/ok/"+title)


# 克里金插值测试
outKrig = Kriging(r"D:/shp_data/0_10_t_p.shp", "meanrfl30", KrigingModelOrdinary("CIRCULAR", 2000, 2.6, 542, 0), 2000, RadiusFixed(20000, 12))
outKrig.save(r"D:/shp_data/t/meanrfl30_0_10")




# 点文件提取栅格图像插值
pool = ['meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET']
for t in range(4):
    for m in ["sp","su","au","wi"]:
        for name in pool:
            sp = "D:/lp_data/project_data/{}_{}_v_p.shp".format(t,m)
            dp = "D:/lp/topoint/{}_{}_{}".format(name,t,m)
            arcpy.PointToRaster_conversion(sp, name,dp, "MAXIMUM", "", 2000)



"""

3、图像掩模提取

"""

import arcpy
from arcpy import env

# 图像掩模提取
from arcpy.sa import *
env.workspace =r"D:/lp_data/"
pool = ['meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET', 'meanrfl30']

#  循环提取代码
for t in range(4):
    for m in ["sp", "su", "au", "wi"]:
        for name in pool:
            if name == 'meanrfl30':
                title = "{}_{}_{}".format("mf30", t, m)
            else:
                title = "{}_{}_{}".format(name, t, m)
            outExtractByMask = ExtractByMask(r"D:/lp_data/ok/"+title, r"D:/lp_data/Loess Plateau/LoessPlateauRegion/LoessPlateauRegion.shp")
            outExtractByMask.save(r"D:/lp_data/tailor_ok/"+title)



"""
4、点文件提取栅格图像值

"""
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = r"D:/lp_data/"
pool = ['meanrfl30', 'meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET']


for m in  ["sp","su","au","wi"]:
    for t in range(4):
        for  name in pool:
            inPointFeatures = r"D:/lp_data/project_data/{}_{}_v.shp".format(t,m)
            # Set local variables
            if name == 'meanrfl30':
                title = "{}_{}_{}".format("mf30", t, m)
            else:
                title = "{}_{}_{}".format(name, t, m)
            # inPointFeatures = "D:/lp_data/project_data/{}_{}_v.shp".format(m)
            inRaster = r"D:/lp_data/tailor_ok/"+title

            outPointFeatures =  "D:/lp_data/topoint/{}_{}_{}.shp".format(t,m,name)

            # Check out the ArcGIS Spatial Analyst extension license
            arcpy.CheckOutExtension("Spatial")

            # Execute ExtractValuesToPoints
            ExtractValuesToPoints(inPointFeatures, inRaster, outPointFeatures,"INTERPOLATE", "VALUE_ONLY")


"""
5、批量进行栅格图像计算

"""

import arcpy  
from arcpy import env
from arcpy.sa import *  

arcpy.CheckOutExtension("spatial")
arcpy.gp.overwriteOutput=1


#定义相关路径
path = r"D:/lp_data/tailor_ok/"
outpath_year=r"D:/lp_data/tailor_ok/year/"
outpath_year_dif=r"D:/lp_data/tailor_ok/year_dif/" 
outpath_quarter_dif=r"D:/lp_data/tailor_ok/quarter_dif"  

#更改工作空间将
env.workspace = r"D:/lp_data/"
pool = ['meanrf', 'cvrf', 'mtmean', 'mtrange', 'Fal_PET', 'meanrfl30']


#  循环计算季度差值
for t in range(3):
    for m in ["sp", "su", "au", "wi"]:
        for name in pool:
            if name == 'meanrfl30':
                title1 = "{}_{}_{}".format("mf30", t, m)
                title2 = "{}_{}_{}".format("mf30", t+1, m)
            else:
                title1= "{}_{}_{}".format(name, t, m)
                title2= "{}_{}_{}".format(name, t+1, m)

            inraster1 =  Raster(path+title1)
            inraster2 =  Raster(path+title2)
            (inraster2-inraster1).save(outpath_quarter_dif+title)

# 循环计算年度值

for t in range(4):
    for name in pool:
        sum = 0 
        for m in ["sp", "su", "au", "wi"]:
            if name == 'meanrfl30':
                title = "{}_{}_{}".format("mf30", t, m)
            else:
                title= "{}_{}_{}".format(name, t, m)
            
            sum += Rastr(path+title)
            if name in  ['Fal_PET', 'meanrfl30']:
                pass 
            else:
                sum = sum/4
        sum.save(outpath_year+"{}_{}".format(t,name)) 

# 循环计算年度差值
for t in range(3):
    for name in pool:
        title1 = "{}_{}".format(name, t)
        title2 = "{}_{}".format(name, t+1)
        inraster1 =  Raster(path+title1)
        inraster2 =  Raster(path+title2)
        (inraster2-inraster1).save(outpath_year_dif+title)





