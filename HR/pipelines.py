# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient() #实例化
collection = client['tencent']['hr'] #设置数据库和集合

class HrPipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item)) #将item转化为字典保存在mongdb
        return item
