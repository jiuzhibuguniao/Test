# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.loader.processors import MapCompose,Join

import sys
import datetime
import socket
import urllib.parse



class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.woshipm.com']

    def parse(self, response):
        l=ItemLoader(item=PropertiesItem(),response=response)

        l.add_xpath("title","//*[@title]/@title")
        l.add_xpath("image_urls","//*[starts-with(@src,'http://image.woshipm.com')]/@src",MapCompose(lambda i:i.strip()))
        # l.add_xpath("urls","//*[starts-with(@href,'http://www.woshipm.com')]/@href",MapCompose(lambda i:i[22:]))
        return l.load_item()


