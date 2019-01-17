import numpy as np
import matplotlib.pyplot as plt


data=[]

try:
    for i in range(10):
        data.append(i)
    for j in arange(10):
        data.append(j)
finally:
    with open("C:\\Users\\Rooobins\\Desktop\\data.txt",'w+',encoding="UTF-8") as f:
        for row in data:
            f.writelines(str(row)+'\n')
        f.close()
