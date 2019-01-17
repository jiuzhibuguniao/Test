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
                    data.append([row_r_read[0],row_r_read[-2],row_r_read[-1]])
            finally:
                with open(path+file+".txt",'w+') as f:
                    for row_data in data:
                        f.writelines(str(row_data)+"\n")
                    f.close()


if __name__=="__main__":
    path="./CSV/"
    loadData(path)

