# -*- coding: utf-8 -*-
from datetime import datetime
from scrapy.spiders import CrawlSpider
from boardgamecrawler.items import Boardgame, BoardgameMeta


class BoardgameSpider(CrawlSpider):
    version = 1.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meta = self.setup_meta()

    def setup_meta(self):
        meta = BoardgameMeta()
        meta['shop_name'] = self.name
        meta['spider_name'] = str(self.__class__)
        meta['version'] = self.version
        meta['extracted_date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return meta