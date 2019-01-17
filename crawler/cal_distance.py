import numpy as np
import math

# 计算两个经纬度之间的距离
def distCalculation(vecA, vecB):
    Lat1 = math.radians(vecA[1])
    Lat2 = math.radians(vecB[1])
    a = Lat1 - Lat2
    b = math.radians(vecA[0]) - math.radians(vecB[0])
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1) * math.cos(Lat2) * math.pow(math.sin(b / 2), 2)))
    distance = s * 6378137
    return distance





left_lng =112.397233
top_lat =38.042581
right_lng =112.69159
bottom_lat =37.728167

offset = 0.002



# lat_range = np.arange(top_lat, bottom_lat, -offset)
# for lat in lat_range:
#     lng_range = np.arange(left_lng, right_lng, offset)
#     for lon in lng_range:
#


dist_1=distCalculation([112.397233,38.042581],[112.397233,38.042581-0.002])
dist_2=distCalculation([112.397233,38.042581],[112.397233-0.002,38.042581])


print(dist_1)
print('\n')
print(dist_2)
