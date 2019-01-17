################################
#csv-json
#Author:@Rooobins
#Date:2018-12-28
################################
import os
import csv
import json

def loadData(path):
    for file in os.listdir(path):
        with open(path+file,'r',encoding="UTF-8") as f:
            data=[]
            f_read=csv.reader(f)
            try:
                for row_r_read in f_read:
                    dic = {}
                    dic["bikeIds"]=row_r_read[0]
                    dic["bikeType"]=row_r_read[1]
                    dic["distId"]=row_r_read[2]
                    dic["distNum"]=row_r_read[3]
                    dic["type"]=row_r_read[4]
                    dic["x"]=row_r_read[5]
                    dic["y"]=row_r_read[6]
                    data.append(dic)
            finally:
                with open(path+file+".json",'w+') as f:
                    json.dump(data,f)
                    print("加载文件完成！")
                    f.close()


if __name__=="__main__":
    path="./CSV/"
    loadData(path)

