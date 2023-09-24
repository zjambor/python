import threading
import requests
from lxml import html

class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        self._symbol = 'AAPL'
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        print(self._url)
        self.start()

    def run(self):
        r = requests.get(self._url)
        if r.status_code != 200:
            print(r.status_code)
            return
        page_contents = html.fromstring(r.text)
        print(page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]'))
        #price = float(page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text)
        #print(price)

