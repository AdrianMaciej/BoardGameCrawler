# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from boardgamecrawler.items import Boardgame, BoardgameData
from boardgamecrawler.spiders import BoardgameSpider


class PlanszostrefaSpider(BoardgameSpider):
    name = 'planszostrefa'
    allowed_domains = ['https://www.planszostrefa.pl', 'planszostrefa.pl']
    start_urls = ['https://planszostrefa.pl']

    rules = (
        #Rule(LinkExtractor(allow=(r'/pl/c/[\w\-\.]*/[\d]+(/)*[\d]*$')), callback='parse_items', follow=True),
        Rule(LinkExtractor(allow=(r'/pl/c/CROWDFUNDING/[\d]+(/)*[\d]*$')), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        for product in response.css('div.product'):
            data = BoardgameData()
            data['name'] = product.css('span.productname::text').get()
            data['url'] = product.css('a.prodname::attr(href)').get()
            data['price'] = product.css('div.price em::text').get()
            data['oldprice'] = product.css('div.price del::text').get()
            avail = product.css('p.avail span.availability::text').getall()
            avail.append(product.css('span.delivery::text').get())
            data['availability'] = ' '.join([f.strip() for f in avail if f])
            data['add_to_cart_available'] = product.css('form.basket input::attr(value)').get()
            yield Boardgame.create(self.meta, data)
