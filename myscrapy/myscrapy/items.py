# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pic = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    show_date = scrapy.Field()
    score = scrapy.Field()
