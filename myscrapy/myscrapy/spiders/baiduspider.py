# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        item = response.xpath('//table//tr/td[2]/div/a/@href').extract()
        with open('data.txt', 'w', encoding='utf8') as f:
            for s in item:
                f.write(s+'\n')
