################################
#txt-to-data
#Author:@Rooobins
#Date:2018-12-28
################################



import numpy as np
import json
import os
import math
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams

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
    data_dic={}                         #结果字典序列
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
            data_dic[row_data_1_bikeIds]=distCalculation(data_1[index_1],data_2[index_2])
    return data_dic

#统计字典数据
def statisticData(data_dic):
    statistic_data={'0':0,"1000":0,"2000":0,"3000":0,"4000":0,"5000":0,"6000":0,"7000":0,"8000":0,"9000":0,"10000":0,">10000":0}
    for row_data_dic in data_dic:
        if 0<=data_dic[row_data_dic]<10:
            statistic_data["0"]+=1
        elif data_dic[row_data_dic]<1000:
            statistic_data["1000"]+=1
        elif data_dic[row_data_dic]<2000:
            statistic_data["2000"]+=1
        elif data_dic[row_data_dic]<3000:
            statistic_data["3000"]+=1
        elif data_dic[row_data_dic]<4000:
            statistic_data["4000"]+=1
        elif data_dic[row_data_dic]<5000:
            statistic_data["5000"]+=1
        elif data_dic[row_data_dic]<6000:
            statistic_data["6000"]+=1
        elif data_dic[row_data_dic]<7000:
            statistic_data["7000"]+=1
        elif data_dic[row_data_dic]<8000:
            statistic_data["8000"]+=1
        elif data_dic[row_data_dic]<9000:
            statistic_data["9000"]+=1
        elif data_dic[row_data_dic]<10000:
            statistic_data["10000"]+=1
        else:
            statistic_data[">10000"]+=1
    return statistic_data


#直方图
def shapeMap_histogram(statistic_data):
    label=[]
    value=[]
    for row_statistic_data in statistic_data:
        value.append(statistic_data[row_statistic_data])
        label.append(row_statistic_data)
    fig1 = plt.figure(2)
    rects = plt.bar(left=(1,2,3,4,5,6,7,8,9,10,11), height=(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10],)  ,width=0.2, align="center", yerr=0.000001)
    plt.title('Test')
    plt.xticks((1,2,3,4,5,6,7,8,9,10,11), ('0', '1000','2000','3000','4000','5000','6000','7000','8000','9000','10000','>10000'))
    plt.show()


if __name__=="__main__":
    path="./txt/"
    data=loadData(path)
    data_dic=compareData(data,0,9)
    statistic_data=statisticData(data_dic)
    print(statistic_data)
    # shapeMap_histogram(statistic_data)