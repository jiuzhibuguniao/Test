##############################
#file read
#Author:Rooobins
#Date:2018-12-06
##############################


# import os
# path = "C:\\Users\\Rooobins\\Desktop\\file" #文件夹目录
# files= os.listdir(path) #得到文件夹下的所有文件名称
# s = []
# for file in files: #遍历文件夹
#      if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#           print(path+"\\"+file+"\n")



##############################
# rename file
##############################
import os
from nt import chdir
path="C:\\Users\\Rooobins\\Desktop\\Data_total\\"
# files=os.listdir(path)
#
#
#
# for file in files:
#     # chdir(os.path.dirname(file))
#     newname=file[0:20]+"txt"
#     os.rename(os,newname)
#     # renameF(file,file[0:20]+"txt")

for file in os.listdir(path):
    newName=file[0:20]+"txt"
    os.rename(os.path.join(path,file),os.path.join(path,newName))