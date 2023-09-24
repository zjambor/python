import requests
from bs4 import BeautifulSoup
import lxml

class WikiWorker():
    def __init__(self):
        self._url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')
        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip('\n')
            yield symbol

# //*[@id="constituents"]/tbody/tr[44]/td[1]/a      //*[@id="constituents"]/tbody/tr[1]/td[1]/a

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print("Couldn't get entries")
            return []

        yield from self._extract_company_symbols(response.text)
    