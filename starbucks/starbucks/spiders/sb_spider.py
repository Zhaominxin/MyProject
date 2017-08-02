import scrapy
from starbucks.items import StarbucksItem
import re


class StarbucksSpider(scrapy.Spider):
    name = 'sb'
    allowed_domains = ['starbucks.com']
    start_urls = [
        'https://www.starbucks.com/menu/catalog/product?drink=refreshers#view_control=product'
        ]


    def parse(self, response):
        p = r'=.+?\b'
       # print('UUUUUUUUUUUU',response.url)

        filename = re.findall(p,response.url)[0][1:]
        #print('FFFFFFFFFFFFFF', filename)

        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.selector.Selector(response)
        names = sel.xpath('//strong/span/text()').extract()
        links = sel.xpath('//ol[@class="blocks blocks-four-up thumbs"]/li/a/@href').extract()
        #print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL',links)

        items = []
        for i in range(len(names)):

            item = StarbucksItem()
            item['drink_name']=(names[i])
            item['drink_link']=(links[i])
            items.append(item)

        return  items