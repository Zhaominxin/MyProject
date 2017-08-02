
import json
import scrapy
from starbucks.items import StarbucksItem
import re

urls  = []

with open('C:\\Users\zmx\Desktop\starbucks\\urls_from_homepage.json') as f :

    target = json.load(f)

    for each in target:
        if 'http' in each['product_link']:
            urls.append(each['product_link'])

print('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU',urls)




class StarbucksSpider(scrapy.Spider):
    name = 'sb4'
    allowed_domains = ['starbucks.com']
    start_urls = urls


    def parse(self, response):

        filename = response.url.split('?')[0].split('/')[-1]
        if filename ==  '':
            filename = 'unsure_name'



        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.selector.Selector(response)
        links = sel.xpath('//a[@class="product-card--grid__name-link"]/@href').extract()
        names = sel.xpath('//div[@class="product-card--grid__name"]/text()').extract()

        print('LLLLLLLLLOOOOOOOOOFFFFFFFFFFFNNNNNNNNNNNN',len(links))
        print('LLLLLLLLLOOOOOOOOOFFFFFFFFFFFDDDDDDDDDDDDD',len(names))

        if len(links) == len(names):

            items = []
            for i in range(len(names)):
                item = StarbucksItem()
                item['product_name']=(names[i])
                item['product_link']=(links[i])
                items.append(item)

        return  items