#canopy算法
import numpy as np
import math



#加载数据
def loadData(filename):
    data=[]
    ifs=open(filename,'w+')
    listData=ifs.readlines()
    for line in listData:
        curLine=line.strip('\n').split(',')
        fltLine=list(map(float,curLine))
        data.append(fltLine)
    return data


#计算两个经纬度之间的距离
def distCalculation(vecA,vecB):
    Lat1=math.radians(vecA[0][0,1])
    Lat2=math.radians(vecB[0][0,1])
    a=Lat1-Lat2
    b=math.radians(vecA[0][0,0])-math.radians(vecB[0][0,0])
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1)*math.cos(Lat2)*math.pow(math.sin(b / 2), 2)))
    distance=s*6378137
    return distance


#canopy算法过程



