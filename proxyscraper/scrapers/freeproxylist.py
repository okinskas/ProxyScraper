from random import randint

from proxyscraper.scrapers.basescraper import BaseScraper
from proxyscraper.proxy import Proxy
from time import sleep


class FreeProxyListScraper(BaseScraper):

    def __init__(self):
        name = 'FreeProxyList'
        url = 'https://free-proxy-list.net/'
        super().__init__(name, url)
        self._driver = None

    def _get_page(self):
        print('getting page...')
        self.driver.get(self.url)
        sleep(randint(3, 4))

    def _manip_table(self):
        print('manipulating page...')
        element = self.driver.find_element_by_css_selector('#proxylisttable_length > label > select')
        last = element.find_elements_by_tag_name('option')[-1]
        self.driver.execute_script('arguments[0].setAttribute("value", 300)', last)
        last.click()

    def _scrape(self):
        print('scraping page...')
        element = self.driver.find_element_by_css_selector('#proxylisttable > tbody')
        results = []
        all_rows = [i for i in element.find_elements_by_xpath('./tr')]
        for i in all_rows:
            elements = i.find_elements_by_xpath('./td')
            current = Proxy(
                ip=elements[0].text,
                port=elements[1].text,
                code=elements[2].text,
                country=elements[3].text,
                anon=elements[4].text)
            results.append(current)
        return results

    def get_proxy_list(self):
        self._start_driver()
        self._get_page()
        self._manip_table()
        proxies = self._scrape()
        self._close_driver()
        return proxies

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver
