# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StocksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()
    security = scrapy.Field()
    sector = scrapy.Field()
    headquarters = scrapy.Field()
    date_added = scrapy.Field()
