# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy_redis.spiders import RedisSpider
import lxml.html
from RDProgram.items import RdprogramItem
import re


class ReadSpider(RedisSpider):
    name = 'read'
    allowed_domains = ['douban.com']
    #start_urls = ['https://book.douban.com/top250?start=0']
    redis_key = 'read'
	
    url = 'https://book.douban.com/top250?start=0'

    def parse(self, response):
        #print(response.body.decode())
        book_info_group = response.xpath('//tr[@class="item"]')

        for each in book_info_group:
            #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+each.extract())
            item = RdprogramItem()
            data = each.extract()
            name = re.findall('title="(.*?)"',data)
            item['book_name'] = name[0]
            #print(name[0])
            book_info = re.findall('<p class="pl">(.*?)<', data)[0]
            book_info_list = book_info.split('/')
            author = ''
            for i in book_info_list[0:-3]:
                author += i
            item['book_author'] = author
            item['book_press'] = book_info_list[-3]
            #print(book_info_list[-3])
            item['book_publish_date'] = book_info_list[-2]
            item['book_price'] = book_info_list[-1]
            quote = re.findall('<span class="inq">(.*?)<',data)[0]
            item['book_quote'] = quote
            url = re.findall('<a href="(.*?)"', data)[0]
            item['book_url'] = url
            yield scrapy.Request(url, callback=self.parse_book_detail, meta={'item': item})
            #print(author)
            #print(url)
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        #print('AAAAAAAAAAAA', next_page)
        if next_page:
            yield scrapy.Request(next_page[0], callback=self.parse)

    def parse_book_detail(self, response):
        item = response.meta['item']
        summary = response.xpath('//div[@class="intro"]/p/text()').extract()
        item['book_summary'] = '\n'.join(summary)
        #print(item['book_summary'])
        yield item
