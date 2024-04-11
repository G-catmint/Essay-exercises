# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyscrapyPipeline:
    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient()
        self.collection = self.mongo_client['winshang']['winshang']

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        print('保存成功:', item)

    def close_spider(self,spider):
        self.mongo_client.close()