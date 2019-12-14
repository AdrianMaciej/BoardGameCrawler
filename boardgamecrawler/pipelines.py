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

    def process_item(self, item, spider):
        item['add_to_cart_available'] = bool(item['add_to_cart_available'])
        return item
