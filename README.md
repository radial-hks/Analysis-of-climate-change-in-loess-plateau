# Analysisofclimatechangeinloessplateau


## 研究背景

气候变化已对生态系统和社会经济产生深远影响[1]，近年来气候变化特征及未来气候已成为全球各界关心的热点问题。政府间气候变化专门委员会(Intergovernmental Panel on Climate Change，IPCC)第五次评估报告(2014)指出：20 世纪50 年代以来，全球几乎所有地区都出现了不同程度的升温变暖；世界各地都出现了气候变化，而气候变暖是毋庸置疑的[2]。到本世纪末，在估算最保守的排放情境下，全球地表均温可能超过1.5 ℃。在全球变暖的大背景下，我国的均温及降水在近五十年也发生巨大的变化。1951年至2001年年平均气温升高1.1℃，增为温速率0.22℃/(5a),全国平均年降水趋势不明显，但是1956年以来有微弱增多的趋势，且四季呈不同程度增加，冬季与春季上升略微明显[3]。然而，温度、降水的变化存在区域差异性，不同区域尺度上的时空变化所导致的气候变也必将不同。为此在了解全球气候要素变化特征的基础上，针对具体区域的进行气候变化特征分析研究是非常有必要的。黄土高原是半湿润区至半干旱区的过渡带[1]，对于气候变化非常敏感，也是生态环境脆弱带。黄土高原近40年气温增高，降水减少，气象要素变幅加大为根本原因，导致黄土高原区域生态环境趋于恶化的重要原因[9]。


## 研究路线

![研究路线](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/%E7%A0%94%E7%A9%B6%E8%B7%AF%E7%BA%BF.jpg)

## 数据资料与研究方法

### 研究区概况

> 黄土高原位于在中国北方太行山以西，乌鞘岭以东，秦岭以北，长城以南，面积约有65万平方千米，占中国面积7%左右。其海拔在1000至2000米之间，高原包括陕西省、山西省、宁夏回族自治区大部地区和甘肃省、内蒙古自治区、青海省部分地区（100.8～114.6 E，33.7～41.3 N），是中国水土流失最严重的地区。

![研究区](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/dem.jpg)

### 研究数据

####  数据来源及空间分布

> 数据来源于国家气象信息中心负责编制的《中国地面气候资料日值数据集》，“中国地面气候资料日值数据集（V3.0）”包含了中国824个基准、基本气象站1951年1月以来测站气压、气温、降水量、蒸发量、相对湿度、风向风速、日照时数和0cm地温要素的日值数据。

数据选取研究区域内部及周围的气象监测站点共计93个。研究数据空间分布如下：

![测站分布](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/%E6%B5%8B%E7%AB%99%E5%88%86%E5%B8%83.jpg)

#### 数据内容

研究数据的主要内容为整理之后的1980年1月1日至2017年12月31日气象测站的日值数据，主要包括平均气温、日最高气温、日最低气温、平均相对湿度、2020时累计降水量、平均风速及日照时数。

|气象参数|单位|
|:---|:---|
|平均气温|0.1℃|
|日最高气温|0.1℃|
|日最低气温|0.1℃|
|平均相对湿度|1%|
|2020时累计降水量|0.1mm|
|平均风速|0.1m/s|
|日照时数|0.1h|

按气候变化特征的提取与研究数据整体的分布特点，将整个研究划分为四个研究阶段，即将数据划分为四部分，分别是:
* 1980年1月1日至1989年12月31日为第一研究阶段；
* 1990年1月1日至1999年12月31日为第二研究阶段；
* 2000年1月1日至2009年12月31日为第三研究阶段；
* 2010年1月1日至2017年12月31日为第四研究阶段；

###  气候特征参数及研究方法

#### 气候特征

|气候变化特征|英文简称|单位|
|:--|:--|:--|
|月总降水量|meanrf130|mm|
|降水天平均降水量|meanrf2|mm|
|降水天降水量变异系数|cvrf2|—|
|月平均气温|mtmean|℃|
|月平均温差|mtrange|℃|
|月潜在蒸发量[21]|PET|mm|

#### 计算方法

详细内容参见:

[气候变化特征参数提取方法](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/Doc/%E6%B0%94%E5%80%99%E5%8F%98%E5%8C%96%E7%89%B9%E5%BE%81%E5%8F%82%E6%95%B0%E6%8F%90%E5%8F%96%E6%96%B9%E6%B3%95.docx)



#### 插值验证 

> 本文采用实际验证法,使用纳什效率系数（Nash-Sutcliffe efficiency coefficient[26]，）与决定系数（coefficient of determination、）作为插值效果的评价指标。其中NSE 与 值越接近1，表示预测值参考意义越大，即预测值的精度越高[27]。

*内容较为简单,在此不作赘述。*


## 气候变化空间分布特征

###  总降水量

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/mf30_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/meanrf30_year.jpg)
### 降水天平均降水量



![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/meanrf_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/meanrf.jpg)

### 降水天降水量变异系数

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/cvrf_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/cvrf.jpg)

### 平均气温
![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/mtmean_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/mtmean_year.jpg)

### 平均温差

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/mtrange_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/mtrange_year.jpg)

### 潜在蒸发量

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/1/pet_a.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/2/pet.jpg)


## 黄土高原气候变化特征


###  总降水量

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/mf30.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/mf30_1.jpg)


### 降水天平均降水量

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/meanrf.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/meanrf.jpg)


### 降水天降水量变异系数

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/cvrf.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/cvrf.jpg)


### 平均气温

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/mtmean.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/mtmean.jpg)


### 平均温差

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/mt.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/mtrange.jpg)


### 潜在蒸发量

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/3/pet.jpg)

![](https://github.com/radial-hks/Analysis-of-climate-change-in-loess-plateau/blob/master/image/4/pet.jpg)


##  结论分析 

本文利用黄土高原内部及周围93个气象监测站1980年至2017年气象监测数据，计算各测站月总降雨量、月降水平均天降水量、月降水天降水量变异系数、月潜在蒸发量、月平均温差等六项气候变化特征，利用克里金插值方法对各指标进行插值，生成其空间分布数据，采用R2和Nash系数验证了插值精度。基于克里金插值结果，分析了黄土高原各气候指标的空间分布特征及其变化，探明了黄土高原1980-2017年间的气候变化规律。主要结论如下：
> 黄土高原总降雨量主要是由东南向西北依次递减，降水主要在夏季， 占全年总降水量的50%以上；从时间分布来看，1980年至2017年黄土高原年总降水量主要增加趋势，尤其是2010年至2017年相较于2000年至2009年尤为明显，总降水量增加43.06mm。


1.  黄土高原降水天平均降水量主要是东南向西北依次递减，主要集中在夏季，春秋次之，冬季最少，其中整个黄土高原年降水天平均降水量分别为0.6753mm、0.729mm、0.7346mm及0.7855mm，呈现稳定的增加趋势。从时间分布来看，1990年至1999年相较于1980年至1989年黄土高原年降雨天平均降水量，南部部分地区减少；其余地区为不同程度的增加，其中东北及西南部分地区增加最多。2000年至2009年相较于1990年至1999年黄土高原年降雨天平均降水量南部及西北少数地区有少量增加，其余大部分地区为减少，其中西部及东南地区减少最多。2010年至2017年相较于2000年至2009年黄土高原年降雨天平均降水量东南地区减少，西北及北部大部分地区增加，其中西北增加尤为明显。


2. 黄土高原降水天平均降水量变异系数主要分布为从南向北减少，从时间分布来看，1990年至1999年相较于1980年至1989年黄土高原年降水天降水量变异系数为东北及西南增加，东南及西北减少；2000年至2009年相较于1990年至1999年黄土高原年年降水天降水量变异系数为西南减少，西北及其他区域增加；2010年至2017年相较于2000年至2009年黄土高原年年降水天降水量变异系数为西南部分地区增加，其余大部分区域为减少。
   
3. 黄土高原年平均气温主要分布为东南向西北递减，平均年气温依次为-1.45℃、-0.49℃、-0.31℃及-0.1℃；从时间分布来看，1980年至2017年黄土高原年平均温度呈明显的增加趋势。


4. 黄土高原季度平均温差主要分布为由北向南依次递减，其中春季温差最大，冬季次之，夏秋最小, 黄土高原年平均温差依次为12.82℃、13.07℃、12.39℃及8.04℃。从时间分布来看，1990年至1999年相比于1980年至1989年黄土高原平均温差主要为增加趋势，2010年至2017年相比于2000年至2009年、2000年至2009年相比于1990年至1999年平均温差呈减少的趋势。

5. 黄土高原总蒸发量主要为西北向东南递减，春夏最盛,占全年总潜在蒸发量的65%以上，秋冬次之。从时间分布来看，1990年至1999年相比于1980年至1989年与2000年至2009年相比于1990年至1999年黄土高原年总蒸发量主要为增加，其中前者在南部增加较多，后者西南度地区增加较多；2010年至2017年相较于2000年至2009年黄土高原年总蒸发量整体减少，其中西北地区尤为明显。


## 不足与展望

本文利用黄土高原内部及周围气象监测站1980年1月1日至2017年12月31日气象数据，分析月总降水量，降水天平均降水量，降水天降水量变异系数，月平均气温，月平均温差和月潜在蒸发量等六项气候变化特征，分组进行克里金插值与验证，分析各气候变化特征的空间分布特征及变化规律。但是在这个研究过程出现些许不足的地方：

* 在研究阶段划分中，第四研究阶段为2010年～2017年，相较于其他三个研究阶段的时间长度，第四研究阶段的计算值相对而言存在误差。
* 在研究黄土高原气候特征变化时，本文使用的是方法是某个研究阶段对于该阶段前一个研究的气候特征值的差值分析，没有固定的参考，只能分析相对变化趋势。
	
本文研究黄土高原时间分布主要是1980年至 2017年共计93个气象监测站的数据，研究初期筛选数据的过程中考虑数据计算与插值的统一性，并没有选取所有的站点数据。在今后的研究中，可充分使用历史研究数据，研究时间范围可以进一步扩大。
