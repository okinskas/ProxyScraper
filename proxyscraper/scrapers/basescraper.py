from time import sleep
from abc import ABC

from selenium import webdriver


class BaseScraper(ABC):

    def __init__(self, name: str, url: str):
        """Create a scraper with a name, corresponding url endpoint and options dict for mapping methods.

        :param name: (str): Name of scraper.
        :param url (str): Endpoint to interact with.
        """
        self._name = name or 'Base'
        self._url = url or 'BaseUrl'
        self._driver = None

    def _start_driver(self):
        print('starting driver...')
        chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        sleep(4)

    def _close_driver(self):
        print('closing driver...')
        self.driver.quit()
        print('closed!')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver