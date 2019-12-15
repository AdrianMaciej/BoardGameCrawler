# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re
import logging

logger = logging.getLogger(__name__)


class PriceRegexPipeline():
    patt = re.compile('([\d\.,]*)')

    def __process_price(self, item, price):
        if price in item.keys():
            p = item[price]
            if p:
                val = self.patt.match(p).group(0)
                val = val.replace(',' ,'.')
                try:
                    val = float(val)
                    item[price] = val
                except Exception as ex:
                    logger.error(ex)
    
    def process_item(self, item, spider):
        self.__process_price(item, 'price')
        self.__process_price(item, 'oldprice')
        return item

class AddToCartPipeline():
    field_name = 'add_to_cart_available'

    def process_item(self, item, spider):
        if self.field_name in item:
            item[self.field_name] = bool(item[self.field_name])
        return item
