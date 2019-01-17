###################################
# 经纬度位置可视化
# Author:Rooobins
# Date:2018-12-8
###################################


# Written by Vamei, http://www.cnblogs.com/vamei/
# Feel free to use or modify this script.
# mpl_toolkits.__path__.append('F:\\Python\\Lib\\mpl_toolkits\\')
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np
#
# # ============================================# read data
# names = []
# pops = []
# lats = []
# lons = []
# countries = []
# # for line in file("../data/major_city"):
# #     info = line.split()
# #     names.append(info[0])
# #     pops.append(float(info[1]))
# #     lat = float(info[2][:-1])
# #     if info[2][-1] == 'S': lat = -lat
# #     lats.append(lat)
# #     lon = float(info[3][:-1])
# #     if info[3][-1] == 'W': lon = -lon + 360.0
# #     lons.append(lon)
# #     country = info[4]
# #     countries.append(country)
#
#
# with open("C:\\Users\\Rooobins\\Desktop\\city.txt","r+") as f:
#     f_1=f.readlines()
#     for line in f_1:
#         info = line.strip("\n").split()
#         names.append(info[0])
#         pops.append(float(info[1]))
#         lat = float(info[2][:-1])
#         if info[2][-1] == 'S': lat = -lat
#         lats.append(lat)
#         lon = float(info[3][:-1])
#         if info[3][-1] == 'W': lon = -lon + 360.0
#         lons.append(lon)
#         country = info[4]
#         countries.append(country)
#
# # ============================================
# # set up map projection with
# # use low resolution coastlines.
# map = Basemap(projection='ortho', lat_0=35, lon_0=120, resolution='l')
# # draw coastlines, country boundaries, fill continents.
# map.drawcoastlines(linewidth=0.25)
# map.drawcountries(linewidth=0.25)
# # draw the edge of the map projection region (the projection limb)
# map.drawmapboundary(fill_color='#689CD2')
# # draw lat/lon grid lines every 30 degrees.
# map.drawmeridians(np.arange(0, 360, 30))
# map.drawparallels(np.arange(-90, 90, 30))
# # Fill continent wit a different color
# map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)
# # compute native map projection coordinates of lat/lon grid.
# x, y = map(lons, lats)
# max_pop = max(pops)
# # Plot each city in a loop.
# # Set some parameters
# size_factor = 80.0
# y_offset = 15.0
# rotation = 30
# for i, j, k, name in zip(x, y, pops, names):
#     size = size_factor * k / max_pop
#     cs = map.scatter(i, j, s=size, marker='o', color='#FF5600')
#     plt.text(i, j + y_offset, name, rotation=rotation, fontsize=10)
#
# plt.title('Major Cities in Asia & Population')
# plt.show()
#
#
#
#
#






#################################################
#smopy画图
#Author:Rooobins
#Date:2018-12-8
#################################################

# import smopy
# hz = smopy.Map((30.0, 119.8, 30.55, 120.5),z=10)
# hz.show_ipython()


# import smopy
# map = smopy.Map((42., -1., 55., 3.), z=4)
# map.save_png("C:\\Users\\Rooobins\\Desktop\\test.png")




#################################################
#folium画图
#Author:Rooobins
#Date:2018-12-8
#################################################


import folium
map_osm = folium.Map(location=[37.68658075,112.4631989])
map_osm.save('C:\\Users\\Rooobins\\Desktop\\osm.html')

# stamen = folium.Map(location=[112.4626148,38.05205064], tiles='Stamen Toner',
# zoom_start=13)
# stamen.save('C:\\Users\\Rooobins\\Desktop\\stamen_toner.html')

# import folium
#
# map_osm=folium.Map(location=[112.4626148,38.05205064], zoom_start=6, tiles='Stamen Terrain')
# folium.Marker([45.463612, 29.294559], popup='Solar Power Station').add_to(map_osm)
#
# map_osm.save('C:\\Users\\Rooobins\\Desktop\\spst.html')