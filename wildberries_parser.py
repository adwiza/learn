import logging
import requests
import bs4
import lxml

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wilberries')


class Client:

    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept-Language': 'ru',
        }

    def load_page(self, page: int=None):
        url = 'https://www.wildberries.ru/search?text=%D1%88%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D1%8B%' \
              'D0%B9%20%D0%BF%D0%BB%D0%B0%D1%82%D0%BE%D0%BA'
        result = self.session.get(url=url)
        result.raise_for_status()
        return result.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parser.run()