################################
#json-data
#Author:@Rooobins
#Date:2018-12-28
################################



import numpy as np
import json
import os
import math

#加载数据
def loadData(path):
    data=[]
    for file in  os.listdir(path):
        currData=[]
        with open(path+file) as f:
            currJson=json.load(f)
            for row_currJson in currJson:
                currData.append([row_currJson["bikeIds"],row_currJson["x"],row_currJson["y"]])
        data.append(currData)
    return data


#计算距离
def distCalculation(vecA, vecB):
    Lat1 = math.radians(float(vecA[:,1]))
    Lat2 = math.radians(float(vecB[:,1]))
    a = Lat1 - Lat2
    b = math.radians(float(vecA[:,0])) - math.radians(float(vecB[:,0]))
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1) * math.cos(Lat2) * math.pow(math.sin(b / 2), 2)))
    distance = s * 6378137
    return distance


#比较
def compareData(data,i,j):
    data_dic={}                         #结果字典序列
    data_1=np.mat(data[i])[:,1:3]       #单车1 经纬度数据集
    data_2=np.mat(data[j])[:,1:3]       #单车2 经纬度数据集
    data_1_bikeIds=[]      #单车1编号数据集
    data_2_bikeIds=[]      #单车2编号数据集
    for row_1_bikeIds in data[i]:
        data_1_bikeIds.append(row_1_bikeIds[0])
    for row_2_bikeIds in data[j]:
        data_2_bikeIds.append(row_2_bikeIds[0])
    for row_data_1_bikeIds in data_1_bikeIds:
        if row_data_1_bikeIds in data_2_bikeIds:
            index_1=data_1_bikeIds.index(row_data_1_bikeIds)
            index_2=data_2_bikeIds.index(row_data_1_bikeIds)
            data_dic[row_data_1_bikeIds]=distCalculation(data_1[index_1],data_2[index_2])
    return data_dic




if __name__=="__main__":

    path="./json/"
    data=loadData(path)
    data_dic=compareData(data,2,3)
    print(len(data_dic))







