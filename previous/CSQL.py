# /usr/bin/env python
# -*- coding:utf-8 -*-
import re  # 导入正则模块
import requests  # 导入http客户端库
import lxml.html  # 基于libxml2这一XML解析库的Python封装，该模块使用C语言编写，解析速度比beautiful soup更快
import pymssql  # 导入Python的SQL Server模块
import importlib

import sys



class SQLServer:
    def __init__(self, host, user, pwd, db):  # 初始化构造方法
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):  # 获取SQL Server数据库连接
        if not self.db:
            raise (NameError, "没有设置数据库连接信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "数据库连接失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()  # 以tuple列表的形式返回结果集中的全部数据
        self.conn.close()  # 关闭查询执行连接
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def spider_blog(url):
    html = requests.get(url).content.decode('utf-8')  # 以utf-8编码格式打开url获取到的html
    tree = lxml.html.fromstring(html)
    list_ordinal = []
    list_index = []
    list_value = []
    i = 0
    while i < len(tree.cssselect('.link_title')):  # css选择器抽取.link_title元素并替换掉回车换行及空格
        list_index.append(tree.cssselect('.link_title')[i].text_content().replace('\r\n', '').replace(' ', ''))
        list_ordinal.append(i + 1)  # 追加元素到列表
        i += 1
    etl_value = re.findall(r'<span class="link_title"><a href="(.*?)">', html, re.S)  # 正则解析提取URL
    cut_url = url.replace('/' + url.split('/')[-1], '')  # 切片拆分拼接完整url
    for value in etl_value:
        list_value.append((cut_url + value).replace('\r\n', '').replace(' ', ''))
    return zip(list_ordinal, list_index, list_value)  # 合并三个列表元素


def main():
    mscon = SQLServer(host="ROOOBINS-PC", user="sa", pwd="w*K19910909", db="BlogDB")  # 目标SQLServer数据库配置信息
    results = spider_blog('http://blog.csdn.net/binguo168?viewmode=contents')  # 测试抓取的博客URL
    for ordinal, key, value in results:
        print()
        str(ordinal) + '\t' + key + '\t' + value
        sql = "INSERT INTO dbo.Blog_Message(Title,BlogURL) VALUES('" + key + "','" + value + "')"
        mscon.ExecNonQuery(sql)


if __name__ == '__main__':
    main()

