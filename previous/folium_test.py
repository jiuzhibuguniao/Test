###################################
#地理位置可视化
#Author:Rooobins
#Date:2018-12-12
###################################

import numpy as np
import folium
from folium.plugins import HeatMap

# data_canopy=[]
# with open("C:\\Users\\Rooobins\\Desktop\\Data_canopy\\operrecord_18062118_canopy.txt","r",encoding="UTF-8") as f:
#     f_read=f.readlines()
#     for ls in f_read:
#         currData=ls.strip("\n").split(",")
#         currData_canopy=list(map(float,currData))
#         currData_canopy.reverse()
#         data_canopy.append(currData_canopy)
#     f.close()
#
#     map_osm = folium.Map(location=[37.68658075, 112.4631989],zoom_start=10)
#     HeatMap(data_canopy).add_to(map_osm)
#     map_osm.save('C:\\Users\\Rooobins\\Desktop\\heatMap.html')


###################################################################################################
# data_kmeans_centroids=[]
# data_kmeans_centroids_end=[]
# with open("C:\\Users\\Rooobins\\Desktop\\Data_canopy\\operrecord_18062118_kmeans_centroids.txt","r",encoding="UTF-8")  as f:
#     f_read=f.readlines()
#     # print(f_read)
#     for line in f_read:
#         currData=line.strip("[]\n  ").split(" ")
#         # if '' in currData:
#         #     del currData[currData.index('')]
#         #第一次清除空值
#         for row in currData:
#             if row=='':
#                 del currData[currData.index(row)]
#             # else:
#             #     continue
#         data_kmeans_centroids.append(currData)
#         # print(currData)
#     f.close()
#     #第二次清除空值
#     for line in data_kmeans_centroids:
#         for row in line:
#             if row=="":
#                 del line[line.index(row)]
#     #第三次清除空值
#     for line in data_kmeans_centroids:
#         for row in line:
#             if row=="":
#                 del line[line.index(row)]
#     # for line in data_kmeans_centroids:
#     #     print(line)
#
#     #data_kmeans_centroids字符串列表转化为浮点数列表
#     for line in data_kmeans_centroids:
#         curData=list(map(float,line))
#         curData.reverse()    #反转列表值
#         data_kmeans_centroids_end.append(curData)   #最终得到的列表
#
#     # for line in data_kmeans_centroids_end:
#     #     print(line)
#     #地理位置可视化
#     map_osm = folium.Map(location=[37.68658075, 112.4631989],zoom_start=10)
#     HeatMap(data_kmeans_centroids_end).add_to(map_osm)
#     map_osm.save('C:\\Users\\Rooobins\\Desktop\\operrecord_18062118_kmeans_centroids.html')
##################################################################################################

#爬取到的太原市共享单车总的位置信息
data=[]
with open("C:\\Users\\Rooobins\\Desktop\\map.txt","r",encoding="UTF-8") as f:
    f_read=f.readlines()
    for row in f_read:
        currData=row.strip("\n").split(",")   #截取有效位置信息
        cData=list(map(float,currData))       #字符型列表转换为浮点型列表
        data.append(cData)
    map_osm = folium.Map(location=[37.68658075, 112.4631989],zoom_start=20)
    print(data)
    HeatMap(data).add_to(map_osm)
    map_osm.save('C:\\Users\\Rooobins\\Desktop\\map.html')
