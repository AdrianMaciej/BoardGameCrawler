# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from boardgamecrawler.items import Boardgame


class PlanszostrefaSpider(CrawlSpider):
    name = 'planszostrefa'
    allowed_domains = ['https://www.planszostrefa.pl', 'planszostrefa.pl']
    start_urls = ['https://planszostrefa.pl']

    rules = (
        Rule(LinkExtractor(allow=(r'/pl/c/[\w\-\.]*/[\d]+(/)*[\d]*$')), callback='parse_items', follow=True),
        #Rule(LinkExtractor(allow=(r'/pl/c/CROWDFUNDING/[\d]+(/)*[\d]*$')), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        for product in response.css('div.product'):
            item = Boardgame()
            item['shop_origin'] = self.name
            item['name'] = product.css('span.productname::text').get()
            item['url'] = product.css('a.prodname::attr(href)').get()
            item['price'] = product.css('div.price em::text').get()
            item['oldprice'] = product.css('div.price del::text').get()
            avail = product.css('p.avail span.availability::text').getall()
            avail.append(product.css('span.delivery::text').get())
            item['availability'] = ' '.join([f.strip() for f in avail if f])
            item['add_to_cart_available'] = product.css('form.basket input::attr(value)').get()
            yield item
