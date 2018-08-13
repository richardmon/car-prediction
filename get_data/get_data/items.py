# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    id           = scrapy.Field()
    color        = scrapy.Field()
    fuel         = scrapy.Field()
    mileage      = scrapy.Field()
    brand        = scrapy.Field()
    model        = scrapy.Field()
    onlyOwner    = scrapy.Field()
    year         = scrapy.Field()
    steering     = scrapy.Field()
    engine       = scrapy.Field()
    traction     = scrapy.Field()
    transmission = scrapy.Field()
    location     = scrapy.Field()
    image_urls   = scrapy.Field()
    images       = scrapy.Field()
    price        = scrapy.Field()
