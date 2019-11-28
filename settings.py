# -*- coding: utf-8 -*-

import scrapy

class WikidatascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    desc = scrapy.Field()