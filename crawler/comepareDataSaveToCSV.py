#################################
#comepareDataSaveToCSV
#Author:@Rooobins
#Date:2019-1-2
#################################

import numpy as np
import json
import os
import math
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import csv

#加载数据
def loadData(path):
    data=[]
    for file in  os.listdir(path):
        currData=[]
        with open(path+file,'r') as f:
            currTxt=f.readlines()
            for row_currTxt in currTxt:
                temp=row_currTxt.strip("[]\n ").split(",")
                currData.append([eval(temp[0]),float(eval(temp[1])),float(eval(temp[2]))])
        data.append(currData)
    return data


#计算距离
def distCalculation(vecA, vecB):
    Lat1 = math.radians((vecA[1]))
    Lat2 = math.radians((vecB[1]))
    a = Lat1 - Lat2
    b = math.radians((vecA[0])) - math.radians((vecB[0]))
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1) * math.cos(Lat2) * math.pow(math.sin(b / 2), 2)))
    distance = s * 6378137
    return distance


#比较
def compareData(data,i,j):
    data_dic=[]                         #结果字典序列
    # data_1=np.mat(data[i])[:,1:3]       #单车1 经纬度数据集
    # data_2=np.mat(data[j])[:,1:3]       #单车2 经纬度数据集

    data_1=[]                             #单车1 经纬度数据集
    data_2=[]                             #单车2 经纬度数据集

    for row_1_data in data[i]:
        data_1.append([row_1_data[1],row_1_data[2]])
    for row_2_data in data[j]:
        data_2.append([row_2_data[1],row_2_data[2]])

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
            distance=distCalculation(data_1[index_1],data_2[index_2])
            if distance>10:
                curr_1=str(str(data_1[index_1][0])+","+str(data_1[index_1][1]))
                curr_2=str(str(data_2[index_2][0])+","+str(data_2[index_2][1]))
                curr_Data=[]
                curr_Data.append(curr_1)
                curr_Data.append(curr_2)
                data_dic.append({"name":row_data_1_bikeIds,"Line":curr_Data})
    return data_dic


#写入csv文件
def write_json(data):
    with open("F:\\data.js",'w+') as json_file:
        json.dump(data,json_file)
        print("successfully")
        json_file.close()





if __name__=="__main__":
    path="./txt/"
    data=loadData(path)
    data_dic=compareData(data,2,3)
    write_json(data_dic)
