################################
#聚类中心平衡度表格
#Author:@Rooobins
#Date:2018-12-25
################################

import math
import os
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xlwt


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

    #新建Excel表格
    f=xlwt.Workbook()
    sheet1=f.add_sheet("Test",cell_overwrite_ok=True)

    path_spider_file="E:\\我的文件\\Data_1\\Data_kmeans_clusterAssment\\"
    data_label=label_invert_int(path_spider_file)
    data_morning_label_index=[i for i in range(len(data_label)) if 0<data_label[i]<12]

    plt.figure(figsize=(20,10),dpi=200)

    x_scale=range(len(data_morning_label_index))

    #加载商业圈数据
    data_business_circle=loadData_number("E:\\我的文件\\business_circle.txt")
    #加载区域聚类中心经纬度
    data_kmeans_centriod=loadData_kmeans_centroid("E:\\我的文件\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_centroids.txt")
    #加载每个聚类中心每次的数量
    data_kmeans_centriod_number=loadData_number("E:\\我的文件\\data.txt")

    i=0

    for row_data_kmeans_centriod  in data_kmeans_centriod:
        min_value=np.inf
        min_index=0
        data_renew=[]
        data_morning=[]
        currData=[]
        line_1=[]
        line_2=[]
        line_3=[]
        data_cache=[]


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
            # # line_1=data_renew[int(len(data_renew)*0.05)]
            # for row_1 in range(len(data_morning)):
            #     line_1.append(data_renew[int(len(data_renew)*0.05)])
            # plt.subplot(8,9,i)
            # plt.plot(x_scale,line_1)
            # plt.plot(x_scale,data_morning,'r')
            # plt.xlabel("times")
            # plt.ylabel("numbers")

            # data_cache.append(row_data_kmeans_centriod)
            # data_cache.append(min_value)
            # data_cache.append(0.05)
            # data_cache.cache.append(data_renew[int(len(data_renew)*0.05)])
            sheet1.write(i,0,str(row_data_kmeans_centriod))
            sheet1.write(i,1,str(min_value))
            sheet1.write(i,2,str(0.05))
            sheet1.write(i,3,str(data_renew[int(len(data_renew)*0.05)]))


        elif min_value<10000:
            # # line_2=data_renew[int(len(data_renew)*0.1)]
            # for row_2 in range(len(data_morning)):
            #     line_2.append(data_renew[int(len(data_renew)*0.1)])
            # plt.subplot(8,9,i)
            # plt.plot(x_scale,line_2)
            # plt.plot(x_scale,data_morning,'r')
            # plt.xlabel("times")
            # plt.ylabel("numbers")
            sheet1.write(i,0,str(row_data_kmeans_centriod))
            sheet1.write(i,1,str(min_value))
            sheet1.write(i,2,str(0.1))
            sheet1.write(i,3,str(data_renew[int(len(data_renew)*0.1)]))

        else:
            # # line_3=data_renew[int(len(data_renew)*0.2)]
            # for row_3 in range(len(data_morning)):
            #     line_3.append(data_renew[int(len(data_renew)*0.2)])
            # plt.subplot(8,9,i)
            # plt.plot(x_scale,line_3)
            # plt.plot(x_scale,data_morning,'r')
            # plt.xlabel("times")
            # plt.ylabel("numbers")
            sheet1.write(i,0,str(row_data_kmeans_centriod))
            sheet1.write(i,1,str(min_value))
            sheet1.write(i,2,str(0.2))
            sheet1.write(i,3,str(data_renew[int(len(data_renew)*0.2)]))
        i=i+1
    f.save("C:\\Users\\Rooobins\\Desktop\\test.xls")


if __name__=="__main__":
    main()












