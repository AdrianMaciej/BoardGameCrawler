# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from boardgamecrawler.items import Boardgame


class TrzytrolleSpider(CrawlSpider):
    name = 'trzytrolle'
    allowed_domains = ['3trolle.pl']
    start_urls = ['https://3trolle.pl/']

    rules = (
        Rule(LinkExtractor(allow=(r'/[\w-]+(/)*(\?p=\d+)*$')), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        for product in response.xpath('//div[@itemtype="https://schema.org/Product"]'):
            item = Boardgame()
            item['shop_origin'] = self.name
            item['name'] = product.css('a.product-name::text').get()
            item['url'] = product.css('a.product-name::attr(href)').get()
            item['price'] = product.css('span.price::text').get()
            item['oldprice'] = product.css('span.old-price::text').get()
            item['availability'] = product.css('div.availability span:nth-child(2)::text').get()
            item['add_to_cart_available'] = product.css('a.ajax_add_to_cart_button::attr(data-id-product)').get()
            yield item
