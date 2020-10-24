import logging
import requests
import bs4
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wilberries')

ParseResut = namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url',
        #'price',
    ),
)

class Client:

    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept-Language': 'ru',
        }
        self.result = []

    def load_page(self, page: int=None):
        url = 'https://www.wildberries.ru/search?text=%D1%88%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D1%8B%' \
              'D0%B9%20%D0%BF%D0%BB%D0%B0%D1%82%D0%BE%D0%BA'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)

        url_block = block.select_one('a.ref_goods_n_p') #  j-open-full-product-card
        if not url_block:
            logger.error('no_url_block')
            return

        base_url = 'https://www.wildberries.ru'
        url = base_url + url_block.get('href')
        if not url:
            logger.error('no href')
            return

        logger.info(f'{url}')

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parser.run()