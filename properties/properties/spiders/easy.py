# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,Join
from properties.items import PropertiesItem

import datetime
import socket
import urllib.parse


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    start_urls = ['http://www.woshipm.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[starts-with(@href,'http://www.woshipm.com')]/@href"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # l=ItemLoader(item=PropertiesItem(),response=response)
        #
	    # l.add_xpath("title","//*[@title]/@title")
	    # l.add_xpath("image_urls","//*[starts-with(@src,'http://image.woshipm.com')]/@src")


        l = ItemLoader(item=PropertiesItem(), response=response)

        l.add_xpath("title", "//*[@title]/@title")
        l.add_xpath("image_urls", "//*[starts-with(@src,'http://image.woshipm.com')]/@src", MapCompose(lambda i: i.strip()))
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return l.load_item()
