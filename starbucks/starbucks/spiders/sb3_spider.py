
import json
import scrapy
from starbucks.items import StarbucksItem


class StarbucksSpider(scrapy.Spider):
    name = 'sb3'
    allowed_domains = ['starbucks.com']
    start_urls = [
        'https://www.starbucks.com/coffee'
        ]


    def parse(self, response):

        filename = 'urls_from_homepage'

        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.selector.Selector(response)
        link = sel.xpath('//ol[@class="blocks blocks-four-up"]/li/ol/li/a/@href').extract()
        name = sel.xpath('//ol[@class="blocks blocks-four-up"]/li/ol/li/a/text()').extract()

        items = []

        print('LLLLLLLLLLLLLLLLLLLLLLLLL',len(link))
        print('NNNNNNNNNNNNNNNNNNNNNNNNNN',len(name))

        if len(link) == len(name):

            for i in range(len(name)):

                item = StarbucksItem()
                item['product_class_name']=(name[i])
                item['product_class_link']=(link[i])
                items.append(item)

        return  items
