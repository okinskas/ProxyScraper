from random import randint

from proxyscraper.scrapers.basescraper import BaseScraper
from time import sleep


class FreeProxyListScraper(BaseScraper):

    def __init__(self):
        name = 'FreeProxyList'
        url = 'https://free-proxy-list.net/'
        super().__init__(name, url)
        self._driver = None

    def get_page(self):
        print('getting page...')
        self.driver.get(self.url)
        sleep(randint(3, 4))

    def manip_table(self):
        print('manipulating page...')
        element = self.driver.find_element_by_css_selector('#proxylisttable_length > label > select')
        last = element.find_elements_by_tag_name('option')[-1]
        self.driver.execute_script('arguments[0].setAttribute("value", 300)', last)
        last.click()

    def scrape(self):
        print('scraping page...')
        element = self.driver.find_element_by_css_selector('#proxylisttable > tbody')
        all_rows = [i.text for i in element.find_elements_by_xpath('./tr')]
        [print(x) for x in all_rows]

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver
