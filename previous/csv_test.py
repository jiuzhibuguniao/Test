###########################################
# CSV TO CSV
#Author:Rooobins
#Date:2018-11-27
###########################################


import csv

with open("C:\\Users\\Rooobins\\Desktop\\operrecord_18062110_center_2.csv","r+") as f:
    f_csv=csv.reader(f)
    with open("C:\\Users\\Rooobins\\Desktop\\operrecord_18062110_center_3.csv","w+",newline='') as f_1:
        f_1_csv=csv.writer(f_1)
        f_1_csv.writerow(["所在省份","经纬度"])
        for row in f_csv:
            f_1_csv.writerow(["山西省",row[0]+","+row[1]])
        f_1.close()
    f.close()


###########################################
# TXT TO CSV
#Author: Rooobins
#Date: 2018-11-28
###########################################

import csv
with open("C:\\Users\\Rooobins\\Desktop\\centroids_1.txt","r+",encoding="UTF-8") as f:
    f_text=f.readlines()
    data=[]
    for row in f_text:
        currRow=row.strip("[]\n ").split("  ")
        data.append(currRow)
    with open("C:\\Users\\Rooobins\\Desktop\\centroids_1.csv","w+",encoding="UTF-8",newline='') as ff:
        ff_csv=csv.writer(ff)
        ff_csv.writerow(["所在省份","经纬度"])
        for line in data:
            ff_csv.writerow(["山西省",str(line[0])+","+str(line[1])])
        ff.close()
    f.close()



###########################################
# matri to txt
#Author:Rooobins
#Date:2018-11-29
###########################################


import numpy as np

with open("C:\\Users\\Rooobins\\Desktop\\test.txt","w+",encoding="UTF-8") as f:
    f_matri=np.mat(np.random.rand(10,2))
    for row in f_matri:
        f.write(str(row)+"\n")
    f.close()



############################################
# string of list to txt
#Author:Rooobins
#Date:2018-11-29
############################################


ls=["wangkai\n","wangzhen\n","zhengyangxian\n","fenyangshi\n"]
with open("C:\\Users\\Rooobins\\Desktop\\test.txt","w+",encoding="UTF-8") as f:
    f.writelines(ls)




############################################
# edit filename
# Author:Rooobins
# Date:2018-12-2
############################################

def editName(i):
    # for ii in range(i):
    return "operrecord_%s"%i


iterator=True
name=[]
i=10
while(iterator):
    if(i<1):
        iterator=False
    else:
        name.append(editName(i))
        i=i-1

for row in name:
    print(row+'\n')


#############################################
# string to float
# Author : Rooobins
# Date : 2018-12-3
#############################################


with open("C:\\Users\\Rooobins\\Desktop\\Data\\operrecord_18120322_canopy.txt","r",encoding="UTF-8") as f:
    data=[]
    for row in f:
        data.append(row)
    data_0=data[0].strip("\n").split(",")
    print(data)
    print(data[0]+"\n")
    print(data_0)







