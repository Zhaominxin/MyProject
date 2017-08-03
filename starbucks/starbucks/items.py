# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StarbucksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    drink_name = scrapy.Field()
    drink_link = scrapy.Field()
    drink_desc = scrapy.Field()
    product_class_name = scrapy.Field()
    product_class_link = scrapy.Field()
    product_link = scrapy.Field()
    product_name = scrapy.Field()
    product_desc = scrapy.Field()
    product_price = scrapy.Field()
