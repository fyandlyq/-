# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class MyscrapyPipeline(object):

    def process_item(self, item, spider):
        os.makedirs(item['name'])
        with open(item['name'] + '\\' + item['name']+'.txt', 'w') as f:
            f.write('电影:' + item['name'] + '\n')
            f.write('导演:' + item['director' + '\n'])
            f.write('演员:' + item['actor' + '\n'])
            f.write('上映时间:' + item['show_date' + '\n'])
            f.write('评分:' + item['score' + '\n'])
            f.write('图片:' + item['pic'] + '\n')
        return item

    # def close_project(self, spider):
    #     self.file.close()
