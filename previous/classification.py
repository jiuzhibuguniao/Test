############################################
#分类出聚类点
#Author:Rooobins
#Date:2018-12-13
#edit date:2018-12-15
############################################
import os
data_end=[]
data_1=[]                                                                                     ##每个聚类点聚类到哪个聚类点
with  open("C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_clusterAssment.txt","r+",encoding="UTF-8")  as f_1:
    f_read_1=f_1.readlines()
    for line_1 in f_read_1:
        currData_1=line_1.strip("\n[] ").split(" ")
        data_1.append(float(currData_1[0]))


data_2=[]                                                                                     ##最终的聚类点
with open("C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_centroids.txt","r+",encoding="UTF-8") as f_2:
    f_read_2=f_2.readlines()
    for line_2 in f_read_2:
        currData_2=line_2.strip("\n[] ").split(" ")
        data_2.append([float(currData_2[0]),float(currData_2[-1])])


data_3=[]                                                                                     ##所有的聚类点
with open("C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_total\\togetherAll_kmeans_center.txt","r+",encoding="UTF-8") as f_3:
    f_read_3=f_3.readlines()
    for line_3 in f_read_3:
        currData_3=line_3.strip("\n[] ").split(",")
        data_3.append([float(currData_3[0]),float(currData_3[-1])])


def loadData(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for line in f_read:
            currData=line.strip("\n[] ").split(" ")
            data.append([float(currData[0]),float(currData[-1])])
    return data



def loadData_1(file):
    data=[]
    with open(file,"r+",encoding="UTF-8") as f:
        f_read=f.readlines()
        for line in f_read:
            currData=line.strip("\n[] ").split(" ")
            data.append(float(currData[0]))
    return data


path_1="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_centroids\\"
path_2="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_clusterAssment\\"
for row in data_2:   #遍历最终的聚类点
    i=0
    ls=[i for i in range(len(data_1)) if data_1[i]==data_2.index(row)]                   #对于每个最终聚类点找出所有包含的小的聚类点的下标
    if ls:                                                                               #判断列表是否为空
        for file  in os.listdir(path_1):                                                 #遍历文件夹下所有小的聚类点TXT文件
            data_4=loadData(path_1+file)                                                 #读取文件夹数据
            for row_ls in ls:                                                            #遍历大聚类下所有的小聚类
                ls_1=[i for i in range(len(data_4)) if data_4[i]==data_3[row_ls]]        #对于每个小聚类点，在data_4中找到对于下标
                if ls_1:
                    data_5=loadData_1(path_2+file[0:26]+"_clusterAssment.txt")
                    for ls_11 in ls_1:
                        i+=data_5.count(ls_11)
                        data_end.append(i)



print(data_end)








