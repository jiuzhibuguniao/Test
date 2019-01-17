################################
#每个聚类点画图
#Author:@Rooobins
#Date:2018-12-16
################################
# import matplotlib.pyplot as plt
# import numpy as np
#
# def loadData(file):
#     data=[]
#     with open(file,"r+",encoding="UTF-8") as f:
#         f_read=f.readlines()
#         for row in f_read:
#             currData=row.strip("[]\n ").split(",")
#             data.append(list(map(float,currData)))
#     return data
#
#
# def showmap(data):
#     x=list(np.arange(74))
#     plt.figure(figsize=(20,20),dpi=200)
#     for i in range(len(data)):
#         plt.subplot(8,9,i+1)
#         y=data[i]
#         plt.plot(x,y,"ro",linewidth=0.1)
#         plt.xlabel("times")
#         plt.ylabel("numbers")
#         plt.title("Broken line diagram")
#     plt.show()
#
#
# def main():
#     file="C:\\Users\\Rooobins\\Desktop\\Data.txt"
#     data=loadData(file)
#     print(data)
#     showmap(data)
#
#
# if __name__=="__main__":
#     main()



###########################################
#画出亲贤街共享单车密度最高的两个图
#Author:@Rooobins
#Date:2018-12-17
###########################################
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import pylab as pl
#
# def loadData(file):
#     data=[]
#     with open(file,"r+",encoding="UTF-8") as f:
#         f_read=f.readlines()
#         for row in f_read:
#             currData=row.strip("[]\n ").split(",")
#             data.append(list(map(float,currData)))
#     return data
#
#
# def label(path):
#     data=[]
#     for file in os.listdir(path):
#         data.append(file[11:19])
#     return data
#
# def label_invert_int(path):
#     data=[]
#     for file in os.listdir(path):
#         currData=file[17:19]
#         data.append(int(float(currData)))
#     return data
#
#
# def showmap(data):
#     x=label_invert_int("C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_clusterAssment\\")
#     x_morning_index=[i for i in range(len(x)) if 1<x[i]<12]
#     data_11=[]
#     data_33=[]
#     for i in x_morning_index:
#         data_11.append(data[10][i])
#     for j in x_morning_index:
#         data_33.append(data[32][j])
#     plt.figure(figsize=(20,20),dpi=200)
#     plt.subplot(1,2,1)
#     plt.plot(x_morning_index,data_11,"r--")
#     pl.xticks(rotation=90)
#     plt.xlabel("times")
#     plt.ylabel("numbers")
#     plt.subplot(1, 2, 2)
#     plt.plot(x_morning_index, data_33, "r--")
#     pl.xticks(rotation=90)
#     plt.xlabel("times")
#     plt.ylabel("numbers")
#     plt.show()
#
#
# def main():
#     file="C:\\Users\\Rooobins\\Desktop\\Data.txt"
#     data=loadData(file)
#     showmap(data)
#
#
#
#
# if __name__=="__main__":
#     main()




####################################################
#读取太原市八个商业圈
#Author:@Rooobins
#Date:2018-12-18
####################################################


# def loadData(file):
#     data=[]
#     with open(file,"r+",encoding="UTF-8") as f:
#         f_read=f.readlines()
#         for row in f_read:
#             currData=row.strip("[]\n ").split(",")
#             data.append(list(map(float,currData)))
#     return data
#
#
# if __name__=="__main__":
#     file="C:\\Users\\Rooobins\\Desktop\\business_circle.txt"
#     data=loadData(file)
#     print(data)
#     print(type(data[0][0]))
#



####################################################
#画出上午每个聚类中心的平衡阈值
#Author:@Rooobins
#Date:2018-12-18
####################################################
import math
import os
import matplotlib.pyplot as plt
import numpy as np

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


#加载区域聚类每次爬取的数量
def loadData_number(file):
    data=[]
    with open(file,"r+",encoding="UTF-8") as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(",")
            data.append(list(map(float,currData)))
    return data


#加载区域中心经纬度
def loadData_kmeans_centroid(file):
    data=[]
    with open(file,"r+",encoding="UTF-8") as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(" ")
            currData.reverse()
            data.append([float(currData[0]),float(currData[-1])])
    return data


#提取所有上午的标签
def label_invert_int(path):
    data=[]
    for file in os.listdir(path):
        currData=file[17:19]
        data.append(int(float(currData)))
    return data



#画图
def main():

    path_spider_file="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_clusterAssment\\"
    data_label=label_invert_int(path_spider_file)
    data_morning_label_index=[i for i in range(len(data_label)) if 0<data_label[i]<12]

    plt.figure(figsize=(20,10),dpi=200)

    x_scale=range(len(data_morning_label_index))

    #加载商业圈数据
    data_business_circle=loadData_number("C:\\Users\\Rooobins\\Desktop\\business_circle.txt")
    #加载区域聚类中心经纬度
    data_kmeans_centriod=loadData_kmeans_centroid("C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_centroids.txt")
    #加载每个聚类中心每次的数量
    data_kmeans_centriod_number=loadData_number("C:\\Users\\Rooobins\\Desktop\\data.txt")

    i=1

    for row_data_kmeans_centriod  in data_kmeans_centriod:
        min_value=np.inf
        min_index=0
        data_renew=[]
        data_morning=[]
        currData=[]
        line_1=[]
        line_2=[]
        line_3=[]


        for row_data_business_circle in data_business_circle:
            distance=distCalculation(row_data_kmeans_centriod,row_data_business_circle)
            if distance<min_value:
                min_value=distance
                min_index=data_business_circle.index(row_data_business_circle)

        currData=data_kmeans_centriod_number[data_kmeans_centriod.index(row_data_kmeans_centriod)]                             #当前的数据

        for row_data_morning_label_index in data_morning_label_index:
            data_morning.append(currData[row_data_morning_label_index])                                                        #筛选出早上的数据
        data_renew=sorted(data_kmeans_centriod_number[data_kmeans_centriod.index(row_data_kmeans_centriod)])                   #排序

        if min_value<5000:
            # line_1=data_renew[int(len(data_renew)*0.05)]
            for row_1 in range(len(data_morning)):
                line_1.append(data_renew[int(len(data_renew)*0.05)])
            plt.subplot(8,9,i)
            plt.plot(x_scale,line_1)
            plt.plot(x_scale,data_morning,'r')
            plt.xlabel("times")
            plt.ylabel("numbers")
        elif min_value<10000:
            # line_2=data_renew[int(len(data_renew)*0.1)]
            for row_2 in range(len(data_morning)):
                line_2.append(data_renew[int(len(data_renew)*0.1)])
            plt.subplot(8,9,i)
            plt.plot(x_scale,line_2)
            plt.plot(x_scale,data_morning,'r')
            plt.xlabel("times")
            plt.ylabel("numbers")
        else:
            # line_3=data_renew[int(len(data_renew)*0.2)]
            for row_3 in range(len(data_morning)):
                line_3.append(data_renew[int(len(data_renew)*0.2)])
            plt.subplot(8,9,i)
            plt.plot(x_scale,line_3)
            plt.plot(x_scale,data_morning,'r')
            plt.xlabel("times")
            plt.ylabel("numbers")

        i=i+1
    plt.show()


if __name__=="__main__":
    main()












