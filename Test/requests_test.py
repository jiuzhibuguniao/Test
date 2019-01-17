import requests
import numpy as np

proxy_pool=[]
with open("F:\\Python\\crawler\\proxy.txt",'r',encoding="UTF-8") as f:
    f_read=f.readlines()
    for row_f_read in f_read:
        currData=row_f_read.strip("\n")
        proxy_pool.append(currData)

proxy = {'http': 'http://' + proxy_pool[np.random.randint(0, len(proxy_pool))],'https': 'https://' + proxy_pool[np.random.randint(0, len(proxy_pool))]}

requests.get("http://www.baidu.com", proxies=proxy)
