import json
import scrapy
from starbucks.items import StarbucksItem
import re

urls  = []

with open('C:\\Users\zmx\Desktop\starbucks\\urls_of_desc.json') as f :

    target = json.load(f)

    for each in target:
        urls.append('https://store.starbucks.com' + each['product_link'])

class StarbucksSpider(scrapy.Spider):
    name = 'sb5'
    allowed_domains = ['starbucks.com']
    start_urls = urls


    def parse(self, response):

        filename = response.url.split('/')[-2]

        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.selector.Selector(response)
        name = sel.xpath('//h1[@class="pdp-order-panel__name"]/text()').extract()
        desc = sel.xpath('//div[@class="pdp__panel--html"]/div/p/text()').extract()
        price = sel.xpath('//span[@class="pdp-order-panel__regular-price"]/text()').extract()


        items = []
        item = StarbucksItem()
        item['product_name']= name
        item['product_desc']= desc
        item['product_price']= price
        items.append(item)

        return items