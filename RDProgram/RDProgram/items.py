# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class RdprogramItem(Item):
    # define the fields for your item here like:

	book_author = Field()
	book_press = Field()
	book_quote = Field()
	book_url = Field()
	book_name = Field()
	book_publish_date = Field()
	book_price = Field()
	book_summary = Field()