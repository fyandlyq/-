# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem

class GetinfoSpider(scrapy.Spider):
    name = 'getinfo'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/27113517/','https://movie.douban.com/subject/27059130/','https://movie.douban.com/subject/26787574/','https://movie.douban.com/subject/26761416/']

    def parse(self, response):
        movie = MyscrapyItem()
        movie['name'] = response.xpath('//div[@id="content"]/h1/span[1]/text()')[0].extract()
        movie['director'] = response.xpath('//div[@id="info"]/span[@class="attrs"]/text()')[0].extract()
        actor_list = []
        actor_list.extend(response.xpath('//span[@class="actor"]'))
