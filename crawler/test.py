################################
#csv-json
#Author:@Rooobins
#Date:2018-12-28
################################
import os
import csv
import json


data=[]
with open("./cluster.txt","r",encoding="UTF-8")  as f:
    f_read=f.readlines()
    for row_f_read in f_read:
        currData=row_f_read.strip("\n ").split(",")
        currJson={}
        currJson["lng"]=currData[0]
        currJson["lat"]=currData[1]
        currJson["count"]=currData[2]
        currJson["lnglat"]="%s,%s"%(currData[0],currData[1])
        data.append(currJson)



with open("./cluster.js","w+") as f:
    json.dump(data,f)
    f.close()