#######################################
#这是一个测试
#Author:@Rooobins
#Date:2018-12-22
#######################################

import pickle
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

import pymysql
import time

def load_url(url, params, timeout, headers=None):
    return requests.get(url, params=params, timeout=timeout, headers=headers).json()


def merge_dicts(*dict_args):
    """
    可以接收1个或多个字典参数
    :param dict_args:
    :return:
    """

    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result




# allloc = []
# """利用高德地图API获取太原所有的小区坐标
# htt://lbs.amap.com/api/webservice/guide/api/search/#text
#     """
#
# with ThreadPoolExecutor(max_workers=5) as executor:
#     url = 'http://api.map.baidu.com/place/v2/search'
#     param = {
#         "key": "8z7GzIaSBj5EzvhyUKCPYM2QZvlzYNiB",   #8z7GzIaSBj5EzvhyUKCPYM2QZvlzYNiB     8z7GzIaSBj5EzvhyUKCPYM2QZvlzYNiB
#         "keywords": "超市",
#         "city": "0351",
#         "citylimit": "true",
#         "output": "json",
#         "page": ""
#     }
#
#     future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
#     for future in futures.as_completed(future_to_url):
#         if future.exception() is not None:
#             print(future.exception())
#         elif future.done():
#             currData=future.result()
#             data = future.result()["pois"]
#             allloc.extend([x["location"] for x in data])
#
#     with open("C:\\Users\\Rooobins\\Desktop\\allloc1.pk", "wb+") as f:
#         pickle.dump(allloc, f, True)



# # if __name__=="__getloc1__":
# #     getloc1()
#
#
def mobai(loc):
    allmobai = []
    try:
        with ThreadPoolExecutor(max_workers=5) as executor:
            url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
                "content-type": "application/x-www-form-urlencoded",
                "referer": "https://servicewechat.com/wx80f809371ae33eda/167/page-frame.html"

            }
            data = {
                "longitude": "",
                "latitude": "",
                "citycode": "0351"
            }

            future_to_url = {
                executor.submit(load_url, url,
                                merge_dicts(data, {"longitude": i.split(",")[0]}, {"latitude": i.split(",")[1]}), 60,
                                headers): url for i in loc
            }

            for future in futures.as_completed(future_to_url):
                if future.exception() is not None:
                    print(future.exception())
                elif future.done():
                    currData=future.result()
                    data = future.result()["object"]
                    allmobai.extend(data)
    # except KeyError:
    #     print("爬虫被封！")
    finally:
        inf = open("C:\\Users\\Rooobins\\Desktop\\all_mobai_position.txt", 'w+')
        for dic in allmobai:
            for idic in dic:
                inf.write(str(dic[idic])+' ')
            inf.write('\n')
        inf.close()


# loc=['112.6128379,37.88403174']
#
#
# mobai1(loc)
#
#
#
#
#
#
# def getloc_Residential():
#     allloc = []
#     """利用高德地图API获取太原所有的小区坐标
#     http://lbs.amap.com/api/webservice/guide/api/search/#text
#     """
#
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         url = "http://restapi.amap.com/v3/place/text"
#         param = {
#             "key": "84ca8f26444f041472f5edcf57272e5e",
#             "keywords": "小区",
#             "city": "0351",
#             "citylimit": "true",
#             "output": "json",
#             "page": ""
#         }
#
#         future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
#         for future in futures.as_completed(future_to_url):
#             if future.exception() is not None:
#                 print(future.exception())
#             elif future.done():
#                 data = future.result()["pois"]
#                 allloc.extend([x["location"] for x in data])
#     return allloc
#
#
# def getloc_bus():
#     allloc = []
#     """利用高德地图API获取太原所有的小区坐标
#     http://lbs.amap.com/api/webservice/guide/api/search/#text
#     """
#
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         url = "http://restapi.amap.com/v3/place/text"
#         param = {
#             "key": "84ca8f26444f041472f5edcf57272e5e",
#             "keywords": "公交车站",
#             "city": "0351",
#             "citylimit": "true",
#             "output": "json",
#             "page": ""
#         }
#
#         future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
#         for future in futures.as_completed(future_to_url):
#             if future.exception() is not None:
#                 print(future.exception())
#             elif future.done():
#                 data = future.result()["pois"]
#                 allloc.extend([x["location"] for x in data])
#     return allloc
#
#
# def getloc_supermarket():
#     allloc = []
#     """利用高德地图API获取太原所有的小区坐标
#     http://lbs.amap.com/api/webservice/guide/api/search/#text
#     """
#
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         url = "http://restapi.amap.com/v3/place/text"
#         param = {
#             "key": "84ca8f26444f041472f5edcf57272e5e",
#             "keywords": "超市",
#             "city": "0351",
#             "citylimit": "true",
#             "output": "json",
#             "page": ""
#         }
#
#         future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
#         for future in futures.as_completed(future_to_url):
#             if future.exception() is not None:
#                 print(future.exception())
#             elif future.done():
#                 data = future.result()["pois"]
#                 allloc.extend([x["location"] for x in data])
#     return allloc
#
#
# print(getloc_supermarket())
#
#
# def getloc_Convenience_Store():
#     allloc = []
#     """利用高德地图API获取太原所有的小区坐标
#     http://lbs.amap.com/api/webservice/guide/api/search/#text
#     """
#
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         url = "http://restapi.amap.com/v3/place/text"
#         param = {
#             "key": "84ca8f26444f041472f5edcf57272e5e",
#             "keywords":"便利店",
#             "city": "0351",
#             "citylimit": "true",
#             "output": "json",
#             "page": ""
#         }
#
#         future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
#         for future in futures.as_completed(future_to_url):
#             if future.exception() is not None:
#                 print(future.exception())
#             elif future.done():
#                 data = future.result()["pois"]
#                 allloc.extend([x["location"] for x in data])
#     return allloc
#
#
# print(getloc_Convenience_Store())
#
#
# def getloc(data):
#     allloc=[]
#     try:
#         for row in data:
#             with ThreadPoolExecutor(max_workers=5) as executor:
#                 url = "http://restapi.amap.com/v3/place/text"
#                 param = {
#                     "key": "95338deed636882b4eca53d73ceb511b",
#                     "keywords": row,
#                     "city": "0351",
#                     "citylimit": "true",
#                     "output": "json",
#                     "page": ""
#                 }
#
#                 future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in
#                                  range(1, 46)}
#                 for future in futures.as_completed(future_to_url):
#                     if future.exception() is not None:
#                         print(future.exception())
#                     elif future.done():
#                         data = future.result()["pois"]
#                         allloc.extend([x["location"] for x in data])
#     except KeyError:
#         print("爬虫被封！")
#     else:
#         with open("C:\\Users\\Rooobins\\Desktop\\end.txt",'w+',encoding="UTF-8") as f:
#             for row in allloc:
#                 f.writelines(str(row)+'\n')
#             f.close()
#
#
#
# data=['公交站','小区','美食','银行','写字楼','超市','便利店','自助餐','电影院','学校','大学','宿舍','研究所','研究院','餐厅','肯德基','麦当劳' ,'中学','小学','公司','食堂','酒店','宾馆','小吃','百货','医院','派出所','公安局','教育局','路口','公寓','KTV','酒吧','景区','公园','汽贸城','民政局','购物中心','教学楼','税务所','税务局','环保局','工商局','小吃街','逸夫楼','政府']
# getloc(data)



# def load_data(file):
#     data=[]
#     with open(file,'r+',encoding="UTF-8") as f:
#         f_read=f.readlines()
#         for row in f_read:
#             data.append(row.strip('\n '))
#     return data

def main():
    # data=load_data("C:\\Users\\Rooobins\\Desktop\\end.txt")
    mobai(['112.566299,38.004921'])
if __name__=='__main__':
    main()
