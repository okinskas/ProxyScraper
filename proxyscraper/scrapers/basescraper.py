from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from typing import Dict


class BaseScraper(ABC):

    def __init__(self, name: str, url: str, data: Dict, options: Dict):
        """Create a scraper with a name, corresponding url endpoint and options dict for mapping methods.

        :param name: (str): Name of scraper.
        :param url (str): Endpoint to interact with.
        :param data (Dict): Form data used in POST request.
        :param options (Dict): Dictionary containing mappings of CSS-selectors and corresponding function to be executed
        """
        self._name = name or 'Base'
        self._url = url or 'BaseUrl'
        self._data = data or {}
        self._options = options or {'': lambda x: x}

    @abstractmethod
    def scrape(self, *args, **kwds):
        """Scrape data from endpoint via given parameters.

        :param args: Variable length argument list.
        :param kwds: Arbitrary keyword arguments.
        :return: List[PlanningResult]: List containing PlanningResults scraped and parsed.
        """
        pass

    def parse_results(self, soup: BeautifulSoup):
        """Parse the results of a HTML page directly in accordance with CSS-selectors and corresponding methods.
        :param soup: (BeautifulSoup): HTML page.
        :return: List[PlanningResult]: List containing PlanningResult objects created from HTML page.
        """
        results = []
        for key in self.options.keys():
            try:
                results += self.options.get(key)(soup.select(key))
            except TypeError:
                continue
        return results

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
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options
