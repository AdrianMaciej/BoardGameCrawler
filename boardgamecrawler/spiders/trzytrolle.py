# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from boardgamecrawler.items import Boardgame, BoardgameData
from boardgamecrawler.spiders import BoardgameSpider


class TrzytrolleSpider(BoardgameSpider):
    name = 'trzytrolle'
    allowed_domains = ['3trolle.pl']
    start_urls = ['https://3trolle.pl/']

    rules = (
        Rule(LinkExtractor(allow=(r'/[\w-]+(/)*(\?p=\d+)*$')), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        for product in response.xpath('//div[@itemtype="https://schema.org/Product"]'):
            data = BoardgameData()
            data['name'] = product.css('a.product-name::text').get()
            data['url'] = product.css('a.product-name::attr(href)').get()
            data['price'] = product.css('span.price::text').get()
            data['oldprice'] = product.css('span.old-price::text').get()
            data['availability'] = product.css('div.availability span:nth-child(2)::text').get()
            data['add_to_cart_available'] = product.css('a.ajax_add_to_cart_button::attr(data-id-product)').get()
            yield Boardgame.create(self.meta, data)
