
import json
import scrapy
from starbucks.items import StarbucksItem
import re

drinklinks  = []

with open('C:\\Users\zmx\Desktop\starbucks\items.json') as f :

    target = json.load(f)

    for each in target:
        drinklinks.append('https://www.starbucks.com/' + each['drink_link'])





class StarbucksSpider(scrapy.Spider):
    name = 'sb2'
    allowed_domains = ['starbucks.com']
    start_urls = drinklinks


    def parse(self, response):

        filename = response.url.split('?')[0].split('/')[-1]
        print('FFFFFFFFFFFFFF', filename)

        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.selector.Selector(response)
        names = sel.xpath('//h1[@class="region size2of3 page_heading"]/text()').extract()
        descs = sel.xpath('//div[@class="region size2of3"]/h2/text()').extract()
        print('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN',names)
        print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL',descs)
        print('LLLLLLLLLOOOOOOOOOFFFFFFFFFFFNNNNNNNNNNNN',len(names))
        print('LLLLLLLLLOOOOOOOOOFFFFFFFFFFFDDDDDDDDDDDDD',len(descs))

        items = []
        for i in range(len(names)):

            item = StarbucksItem()
            item['drink_name']=(names[i])
            item['drink_desc']=(descs[i])
            items.append(item)

        return  items