import sqlite3
import time
import numpy as np


#创建表
# with sqlite3.connect("C:\\Users\\Rooobins\\Desktop\\crawler\\temp.db") as c:
#     c.execute('''CREATE TABLE mobike
#                         (Time DATETIME, bikeIds VARCHAR(12), bikeType TINYINT,distId INTEGER,distNum TINYINT, type TINYINT, x DOUBLE, y DOUBLE)''')


#插入数据
# with sqlite3.connect("C:\\Users\\Rooobins\\Desktop\\crawler\\temp.db") as c:
#     c.execute("INSERT INTO mobike VALUES (%d,'%s',%d,%d,%s,%s,%f,%f)" % (
#         int(time.time()) * 1000, 1212121212, 1, 12121212121212,
#         12, 23, 112,
#         37))


left_lng =112.397233
top_lat =38.042581
right_lng =112.69159
bottom_lat =37.728167

offset = 0.002


data_set=[]


lat_range = np.arange(top_lat, bottom_lat, -offset)
for lat in lat_range:
    lng_range = np.arange(left_lng, right_lng, offset)
    for lon in lng_range:
        data_set.append([lat,lon])


print(len(data_set))