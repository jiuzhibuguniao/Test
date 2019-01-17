# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    image_urls=Field()
    urls=Field()