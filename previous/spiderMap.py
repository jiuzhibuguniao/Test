import pickle
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures




def load_url(url,params,timeout,headers=None):
    return requests.get(url,params=params,timeout=timeout,headers=headers).json()


def merge_dicts(*dict_args):
    """
    可以接收1个或多个字典参数
    :param dict_args:
    :return:
    """

    result={}
    for dictionary in dict_args:
        result.update(dictionary)
    return result



def mobai(loc):
    allmobai=[]
    with ThreadPoolExecutor(max_workers=5) as executor:
        url="https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
        headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
            "content-type":"application/x-www-form-urlencoded",
            "referer":"https://servicewechat.com/wx80f809371ae33eda/167/page-frame.html"

        }
        data={
            "longitude":"",
            "latitude":"",
            "citycode":"0351"
        }

        future_to_url={
            executor.submit(load_url,url,merge_dicts(data,{"longitude":i.split(",")[0]},{"latitude":i.split(",")[1]}),60,headers):url for i in loc
        }

        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data=future.result()["object"]
                allmobai.extend(data)
    inf=open("/root/end.txt",'a+')
    inf.writelines(str(allmobai))
    inf.close()




def getloc():
    allloc=[]
    """利用高德地图API获取太原所有的小区坐标
    http://lbs.amap.com/api/webservice/guide/api/search/#text
    """

    with ThreadPoolExecutor(max_workers=5) as executor:
        url="http://restapi.amap.com/v3/place/text"
        param={
            "key":"84ca8f26444f041472f5edcf57272e5e",
            "keywords":"小区",
            "city":"0351",
            "citylimit":"true",
            "output":"json",
            "page":""
        }

        future_to_url={executor.submit(load_url,url,merge_dicts(param,{"page":i}),60):url for i in range(1,46)}
        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data=future.result()["pois"]
                allloc.extend([x["location"] for x in data])

        with open("/root/allloc.pk","wb") as f:
            pickle.dump(allloc,f,True)


if __name__=="__main__":
    getloc()
    inf=open("/root/allloc.pk","rb")
    allloc=pickle.load(inf)
    inf.close()

    mobai(allloc)




