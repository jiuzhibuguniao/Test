####################################
#数组转化为json
#Author:@Rooobins
#Date:2018-12-27
####################################



# with open("C:\\Users\\Rooobins\\Desktop\\map.txt") as f:
#     data=[]
#     f_read=f.readlines()
#     for row_f_read in f_read:
#         currDic={}
#         currData=row_f_read.strip("[]\n ").split(",")
#         currDic["lnglat"]="%s,%s" % (currData[0],currData[1])
#
#         # currDic["lat"]=currData[1]
#         currDic["count"]=1
#         data.append(currDic)
#     f.close()
#     with open("C:\\Users\\Rooobins\\Desktop\\js_lonlat_test.js","w+",encoding="UTF-8") as f_w:
#         f_w.writelines(str(data))
#         f_w.close()
#     print(data)



# import json
#
#
# array_dic=[{'1':'aaa','2':'bbb'},{'1':'ccc','2':'ddd'}]
#
# # array_dic_1=array_dic.replace("'",'"')
# dic_array={'1':'aaa','2':'bbb'}
# # dic_array_1=dic_array.replace("'",'"')
# # array_dic_dumps=json.loads(array_dic)
# # dic_array_dumps=json.loads(dic_array)
#
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
#
# text_1 = json.dumps(dic_array)
# print(text_1)
# print(type(text_1))
#
#
# text_2=json.dumps(array_dic)
# print(text_2)
# print(type(text_2))


##############################
#json dumps
#Author:@Rooobins
#Date:2019-01-03
##############################

import json
import os
ls=[{'1':1,'2':2}]
with open("./Data/test.js",'w+') as f:
    json.dump(ls,f)
    f.close()