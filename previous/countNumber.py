##################################
#对于每个聚类countNumbers
#Author:@Rooobins
#Date:2018-12-16
##################################

import os
import matplotlib.pyplot as plt
import numpy as np

def loadData_comma_reverse(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(",")
            data.append([float(currData[-1]),float(currData[0])])
    return data



def loadData_space_reverse(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(" ")
            data.append([float(currData[-1]),float(currData[0])])
    return data



def loadData_comma(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(",")
            data.append([float(currData[0]),float(currData[-1])])
    return data



def loadData_space(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(" ")
            data.append([float(currData[0]),float(currData[-1])])
    return data



def loadData_first(file):
    data=[]
    with open(file,"r+",encoding="UTF-8")  as f:
        f_read=f.readlines()
        for row in f_read:
            currData=row.strip("[]\n ").split(" ")
            data.append(int(float(currData[0])))
    return data

def showmap(data):
    x=list(np.arange(74))
    plt.figure(figsize=(20,20),dpi=200)
    for i in range(len(data)):
        plt.subplot(8,10,i+1)
        y=data[i]
        plt.plot(x,y,"r--",linewidth=1)
        plt.xlabel("times")
        plt.ylabel("numbers")
        plt.title("Broken line diagram")
    plt.show()



def main():
    data=[]
    # data_cluster=[]


    file_kmeans_center_kmeans_centroids="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_centroids.txt"
    file_kmeans_center_all="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_total\\togetherAll_kmeans_center.txt"
    file_kmeans_center_kmeans_cluster="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_cache\\Data_canopy\\togetherAll_kmeans_center_kmeans_clusterAssment.txt"


    kmeans_center_kmeans_centroids=[]
    kmeans_center_all=[]
    kmeans_center_kmeans_cluster=[]


    kmeans_center_kmeans_centroids=loadData_space_reverse(file_kmeans_center_kmeans_centroids)
    kmeans_center_all=loadData_comma_reverse(file_kmeans_center_all)
    kmeans_center_kmeans_cluster=loadData_first(file_kmeans_center_kmeans_cluster)                                      #格式唯一


    path_kmeans_centroids="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_centroids\\"
    path_kmeans_cluster="C:\\Users\\Rooobins\\Desktop\\Data_1\\Data_kmeans_clusterAssment\\"


    for row_kmeans_center_kmeans_centroids in kmeans_center_kmeans_centroids:
        data_cluster = []
        list_row_kmeans_center_kmeans_centroids=[i for i in range(len(kmeans_center_kmeans_cluster)) if kmeans_center_kmeans_cluster[i]==kmeans_center_kmeans_centroids.index(row_kmeans_center_kmeans_centroids)]
        if list_row_kmeans_center_kmeans_centroids:
            # for row_list_row_kmeans_center_kmeans_centroids in list_row_kmeans_center_kmeans_centroids:
                for file_path_kmeans_centroids in os.listdir(path_kmeans_centroids):
                    i = 0
                    for row_list_row_kmeans_center_kmeans_centroids in list_row_kmeans_center_kmeans_centroids:
                        data_path_kmeans_centroids=loadData_space(path_kmeans_centroids+file_path_kmeans_centroids)
                        list_data_path_kmeans_centroids=[i for i in range(len(data_path_kmeans_centroids)) if kmeans_center_all[row_list_row_kmeans_center_kmeans_centroids]==data_path_kmeans_centroids[i]]
                        if list_data_path_kmeans_centroids:
                            data_path_kmeans_centroids_kmeans_cluster=loadData_first(path_kmeans_cluster+file_path_kmeans_centroids[0:26]+"_clusterAssment.txt")
                            i+=data_path_kmeans_centroids_kmeans_cluster.count(list_data_path_kmeans_centroids[0])
                    data_cluster.append(i)
                data.append(data_cluster)
        else:
            data.append([0])

    with open("C:\\Users\\Rooobins\\Desktop\\data.txt","w+",encoding="UTF-8")  as ff:
        for row_ff in data:
            ff.writelines(str(row_ff)+"\n")
        ff.close()
    showmap(data)


if __name__=="__main__":
    main()