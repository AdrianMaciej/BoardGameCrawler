# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
from scrapy import Item, Field


class Boardgame(Item):
    shop_origin = Field()
    url = Field()
    name = Field()
    price = Field()
    oldprice = Field()
    availability = Field()
    add_to_cart_available = Field()