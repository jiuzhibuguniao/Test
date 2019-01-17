##############################################
#阿里云运算出来的所有k_means_center汇总
#Author:Rooobins
#Date:2018-12-13
##############################################



import os
from folium.plugins import HeatMap
import folium

data=[]                                                           # 总的数据集
path="C:\\Users\\Rooobins\\Desktop\\Data_kmeans_centroids\\"

for  filetxt in os.listdir(path):
    with open (path+filetxt,'r',encoding="UTF-8")  as f:          #循环读取文件夹下的每个文件
        f_read=f.readlines()
        for line in f_read:
            currData=line.strip("[]\n ").split(" ")
            for row_1 in currData:                                #第一次清洗数据
                if row_1=="":
                    del currData[currData.index(row_1)]
            for row_2 in currData:                                #第二次清洗数据
                if row_2=="":
                    del currData[currData.index(row_2)]
            for row_3 in currData:                                #第三次清洗数据
                if row_3=="":
                    del currData[currData.index(row_3)]
            currData.reverse()
            cData=list(map(float,currData))
            data.append(cData)
# map_osm = folium.Map(location=[37.68658075, 112.4631989],zoom_start=10)         #鸟瞰地图中心点
# HeatMap(data).add_to(map_osm)                                                   #生成热力图
# map_osm.save('C:\\Users\\Rooobins\\Desktop\\togetherAll_kmeans_center.html')

# with open("C:\\Users\\Rooobins\\Desktop\\togetherAll_kmeans_center.txt","w+",encoding="UTF-8")  as f:        #数据写入文件
#     for row in data:
#         f.writelines(str(row)+"\n")
#     f.close()


with open("C:\\Users\\Rooobins\\Desktop\\Data_cache\\togetherAll_kmeans_center.txt","w+",encoding="UTF-8")  as f:
    for row in data:
        f.writelines(str(row[0])+","+str(row[1])+"\n")
    f.close()



