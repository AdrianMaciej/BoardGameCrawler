from scrapy import Item, Field


class BoardgameData(Item):
    url = Field()
    name = Field()
    price = Field()
    oldprice = Field()
    availability = Field()
    add_to_cart_available = Field()


class BoardgameMeta(Item):
    shop_name = Field()
    spider_name = Field()
    version = Field()
    extracted_date = Field()

class Boardgame(Item):
    meta = Field()
    data = Field()
    raw = Field()

    def update(self, key, val):
        '''On update save the original value in the raw schema'''
        self['raw']._values[key], self[key] = self[key], val

    def __getitem__(self, key):
        '''All Fields are taken from the 'data' schema'''
        return self._values[key] if key in self.fields else self._values['data'][key]

    def __setitem__(self, key, value):
        '''All Fields are set on the 'data' schema'''
        if key in self.fields:
            self._values[key] = value
        else:
            self['data'][key] = value

    @staticmethod
    def create(meta, data):
        bg = Boardgame()
        bg['meta'] = meta
        bg['data'] = data
        bg['raw'] = BoardgameData()
        return bg
