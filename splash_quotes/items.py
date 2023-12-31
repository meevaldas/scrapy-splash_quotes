# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join


def clean(s):
    return s[0].replace('\201c', '').replace('\u201d', '').replace('\u00e9', '')


class SplashQuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field(input_processor=clean, output_processor=Join())
    author = scrapy.Field(input_processor=clean, output_processor=Join())
