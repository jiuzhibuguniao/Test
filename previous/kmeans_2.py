#################################
# k-means: 汇总所有的kmeans算法结果，进行canopy算法训练，再进行kmeans算法训练
# Author: Rooobins
# Data: 2018-12-13
#################################

import numpy as np
import time
import math
from datetime import datetime
import os


# 计算两个经纬度之间的距离
def distCalculation(vecA, vecB):
    Lat1 = math.radians(vecA[0][0, 1])
    Lat2 = math.radians(vecB[0][0, 1])
    a = Lat1 - Lat2
    b = math.radians(vecA[0][0, 0]) - math.radians(vecB[0][0, 0])
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1) * math.cos(Lat2) * math.pow(math.sin(b / 2), 2)))
    distance = s * 6378137
    return distance


# 加载数据
def loadDataSet(fileName):  # 解析文件，得到一个浮点数字类型的矩阵
    totalDataMat = []  # 文件的最后一个字段是类别标签
    fr = open(fileName, "r+")
    for line in fr.readlines():
        curLine = line.strip('\n').split(',')
        fltLine = list(map(float, curLine))  # 将每个元素转成float类型
        totalDataMat.append(fltLine)
    return np.mat(totalDataMat)

def main():
    path_1="C:\\Users\\Rooobins\\Desktop\\Data_cache\\Data_total\\"
    path_2="C:\\Users\\Rooobins\\Desktop\\Data_cache\\Data_canopy\\"
    for file in os.listdir(path_1):
        centroids = loadDataSet(path_2+file[0:25]+"_canopy.txt")
        dataSet_1 = loadDataSet(path_1+file)
        k = len(loadDataSet(path_2+file[0:25]+"_canopy.txt"))

        numSamples = dataSet_1.shape[0]
        clusterAssment = np.mat(np.zeros((numSamples, 2)))
        clusterChanged = True

        ## step 1: init centroids
        # centroids = loadDataSet("/root/Data/operrecord_18112822_canopy.txt")

        while clusterChanged:
            clusterChanged = False
            ## for each sample
            for i in range(numSamples):
                minDist = np.inf
                minIndex = 0
                ## for each centroid
                ## step 2: find the centroid who is closest
                for j in range(k):
                    distance = distCalculation(centroids[j, :], dataSet_1[i, :])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j

                ## step 3: update its cluster
                if clusterAssment[i, 0] != minIndex:
                    clusterChanged = True
                    clusterAssment[i, :] = minIndex, minDist ** 2

            ## step 4: update centroids
            for j in range(k):
                pointsInCluster = dataSet_1[np.nonzero(clusterAssment[:, 0].A == j)[0]]
                centroids[j, :] = np.mean(pointsInCluster, axis=0)

        # print('Congratulations, cluster complete!')
        # return centroids, clusterAssment
        #
        # centroids_1, clusterAssment_1 = kmeans(dataSet_1, k_numbers)
        with open(path_2+file[0:25]+"_kmeans_centroids.txt", "w+") as f_1:
            f_1.writelines(str(centroids))
            f_1.close()
        with open(path_2+file[0:25]+"_kmeans_clusterAssment.txt", "w+") as f_2:
            for row in clusterAssment:
                f_2.writelines(str(row)+'\n')
        # f_2.writelines(str(clusterAssment_1))
            f_2.close()




if __name__ == '__main__':
    t_s = datetime.now()
    main()
    t_e = datetime.now()
    usedtime = t_e - t_s
    with open("C:\\Users\\Rooobins\\Desktop\\time.txt",'w+',encoding="UTF-8") as t:
        t.writelines(str(usedtime))
    t.close()







