#####################################
#统计骑行距离数据
#Author:@Rooobins
#Date:2018-12-22
#####################################


# import pandas as pd
#
# f_open=open("C:\\Users\\Rooobins\\Desktop\\operrecord_181130-06-08.csv",'r+',encoding="UTF-8")
# f_csv=pd.read_csv(f_open)
# print(f_csv.ix[0:0])




import math
import matplotlib
import matplotlib.pyplot as plt
import numpy  as np
# 计算两个经纬度之间的距离
def distCalculation(vecA, vecB):
    Lat1 = math.radians(vecA[1])
    Lat2 = math.radians(vecB[1])
    a = Lat1 - Lat2
    b = math.radians(vecA[0]) - math.radians(vecB[0])
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1) * math.cos(Lat2) * math.pow(math.sin(b / 2), 2)))
    distance = s * 6378137
    return distance


# with open("C:\\Users\\Rooobins\\Desktop\\data.txt","r+",encoding="UTF-8") as f:
#     data=[]
#     f_read=f.readlines()
#     for row_f_read in f_read:
#         currData=row_f_read.strip("[]\n ").split("],[")
#         data.append([list(map(float,currData[0].split(","))),list(map(float,currData[1].split(",")))])



#加载数据
def loadData(path):
    data=[]
    with open(path,'r+',encoding="UTF-8") as f:
        f_read=f.readlines()
        for row_f_read in f_read:
            currData = row_f_read.strip("[]\n ").split("],[")
            data.append([list(map(float, currData[0].split(","))), list(map(float, currData[1].split(",")))])
    return data


#汇总数量
def statistic(data):
    dic={"0-0.5":0,'0.5-1':0,'1-2':0,'2-3':0,'3-4':0,"4-5":0,"5-inf":0}
    for row in data:
        if row<=500:
            dic["0-0.5"]+=1
        elif row<=1000:
            dic["0.5-1"]+=1
        elif row<=2000:
            dic["1-2"]+=1
        elif row<=3000:
            dic["2-3"]+=1
        elif row<=4000:
            dic["3-4"]+=1
        elif row<5000:
            dic["4-5"]+=1
        else:
            dic["5-inf"]+=1
    return dic


def showMap(data):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    # plt.hist(data, bins=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000], normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.hist(data, bins=6, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    # 显示横轴标签
    plt.xlabel("区间")
    # 显示纵轴标签
    plt.ylabel("数量")
    # 显示图标题
    plt.title("骑行距离统计图")
    plt.show()

def main():
    path="C:\\Users\\Rooobins\\Desktop\\Data.txt"
    data=loadData(path)
    data_distance=[]
    for row_data in data:
        if abs(distCalculation(row_data[0],row_data[1]))>0:
            data_distance.append(abs(distCalculation(row_data[0],row_data[1])))
    dic=statistic(data_distance)
    data_distance_mat=np.mat(data_distance)
    mask=data_distance_mat<=0
    mask_list=data_distance_mat[mask]
    print(mask_list)
    print(dic)
    # showMap(data_distance)



if __name__=="__main__":
    main()
