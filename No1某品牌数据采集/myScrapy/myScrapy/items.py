# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    _id  = scrapy.Field()
    title = scrapy.Field()
    ceate_time = scrapy.Field()
    Way = scrapy.Field()
    term_cooperation = scrapy.Field()
    area_req = scrapy.Field()
