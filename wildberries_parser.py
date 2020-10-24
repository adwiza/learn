import logging
import requests
import bs4
import csv
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wilberries')

ParseResult = namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'lower_price',
        'discount',
        'url',

    ),
)

HEADERS = (
    'Бренд',
    'Товар',
    'Цена',
    'Скидка',
    'Ссылка',
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
        url_block = block.select_one('a.ref_goods_n_p') #  j-open-full-product-card
        if not url_block:
            logger.error('no_url_block')
            return

        base_url = 'https://www.wildberries.ru'
        url = base_url + url_block.get('href')
        if not url:
            logger.error('no href')
            return

        name_block = block.select_one('div.dtlist-inner-brand-name')
        if not name_block:
            logger.error(f'no name_block on {url}')
            return

        brand_name = name_block.select_one('strong.brand-name')
        if not brand_name:
            logger.error(f'no brand_name on {url}')
            return

        # Clean results
        brand_name = brand_name.text
        brand_name = brand_name.replace('/', '').strip()

        goods_name = name_block.select_one('span.goods-name')
        if not goods_name:
            logger.error(f'no goods_name on {url}')
            return

        # Clean results
        goods_name = goods_name.text
        goods_name = goods_name.replace('/', '').strip()

        price_block = block.select_one('div.j-cataloger-price')
        if not price_block:
            logger.error(f'no price_block on {url}')
            return

        # Clean results
        # price_block = price_block.text
        # price_block = price_block.replace('/', '').strip()

        lower_price = price_block.select_one('ins.lower-price')
        if not lower_price:
            logger.error(f'no lower_price on {url}')
            return

        # Clean results
        lower_price = lower_price.text
        lower_price = lower_price.replace(' ', '').strip()

        discount = price_block.select_one('span.price-sale.active')
        if not discount:
            logger.error(f'no discount on {url}')
            return

        # Clean results
        discount = discount.text
        discount = discount.replace(' ', '').strip()
        discount = discount.replace('-', '').strip()

        self.result.append(ParseResult(
            url=url,
            brand_name=brand_name,
            goods_name=goods_name,
            lower_price=lower_price,
            discount=discount,
        ))
        logger.debug(f'{url} {brand_name} {goods_name} {lower_price} {discount}')
        logger.debug('-' * 100)

    def save_results(self):
        path = 'wildberries_handkerchief.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)
        logger.info(f'Получили {len(self.result)} карточек')

        self.save_results()


if __name__ == '__main__':
    parser = Client()
    parser.run()