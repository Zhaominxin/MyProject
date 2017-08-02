import scrapy

from tutorial.items import DmozItem
#import class from package


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = [
        'http://dmoztools.net/Computers/Systems/HP_3000/',
        'http://dmoztools.net/Computers/Hardware/Systems/IBM/'
        ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        #build response file


        sel = scrapy.selector.Selector(response)

        items = []      

        title = sel.xpath('//div[@class="site-title"]/text()').extract()
        link = sel.xpath('//div[@class="title-and-desc"]/a/@href').extract()
        desc = sel.xpath('//div[@class="site-descr "]/text()').extract()
        desclist = []        

        for i in range(len(desc)):
            if i%2 == 0:
                desclist.append(desc[i])

        for j in range(len(title)):
            item = DmozItem()
            #instantiation
            item['title'] = title[j]
            item['link'] = link[j]
            item['desc'] = desclist[j]

            items.append(item)

        return items

            
        '''titles = sel.xpath('//div[@class="site-title"]/text()').extract()
        links = sel.xpath('//div[@class="title-and-desc"]/a/@href').extract()
        descs = sel.xpath('//div[@class="site-descr "]/text()').extract()
        num = len(titles)
        for i in range(num):
            print(titles[i], links[i], descs[i])'''
